import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from missing_features_helper import DropHighMissingFeatures
from sklearn.model_selection import cross_validate, RepeatedStratifiedKFold
from sklearn.metrics import make_scorer, recall_score, precision_score, f1_score


def constant_near_constant_report(
    X: pd.DataFrame,
    near_constant_threshold: float = 0.98
) -> pd.DataFrame:
    """
    Identify constant and near-constant features in a dataframe.

    Constant feature:
        A column with 0 or 1 unique non-missing values.

    Near-constant feature:
        A column where one value dominates at least near_constant_threshold
        of the non-missing observations.

    Parameters
    ----------
    X:
        Feature dataframe.
    near_constant_threshold:
        Dominance threshold. 0.98 means one value appears in >= 98%
        of non-missing rows.

    Returns
    -------
    report:
        DataFrame with one row per feature and flags for constant/near-constant.
    """

    rows = []

    for col in X.columns:
        s = X[col]
        n_rows = len(s)
        n_missing = s.isna().sum()
        missing_rate = n_missing / n_rows

        non_missing = s.dropna()
        n_non_missing = len(non_missing)

        # Unique values excluding missing values
        n_unique_non_missing = non_missing.nunique()

        # Unique values including NaN as a value
        n_unique_including_missing = s.nunique(dropna=False)

        if n_non_missing == 0:
            most_common_value = np.nan
            most_common_count = 0
            dominance_rate_non_missing = np.nan
            dominance_rate_total = np.nan
        else:
            counts = non_missing.value_counts(dropna=True)
            most_common_value = counts.index[0]
            most_common_count = counts.iloc[0]

            # Among observed values only
            dominance_rate_non_missing = most_common_count / n_non_missing

            # Among all rows, including missing rows in the denominator
            dominance_rate_total = most_common_count / n_rows

        is_constant = n_unique_non_missing <= 1

        is_near_constant = (
            not is_constant
            and dominance_rate_non_missing >= near_constant_threshold
        )

        rows.append({
            "feature": col,
            "n_rows": n_rows,
            "n_missing": n_missing,
            "missing_rate": missing_rate,
            "n_unique_non_missing": n_unique_non_missing,
            "n_unique_including_missing": n_unique_including_missing,
            "most_common_value": most_common_value,
            "most_common_count": most_common_count,
            "dominance_rate_non_missing": dominance_rate_non_missing,
            "dominance_rate_total": dominance_rate_total,
            "is_constant": is_constant,
            "is_near_constant": is_near_constant,
        })

    report = pd.DataFrame(rows)

    return report.sort_values(
        by=["is_constant", "is_near_constant", "dominance_rate_non_missing"],
        ascending=[False, False, False]
    )
    
    
def missingness_by_target_report(X: pd.DataFrame, y: pd.Series) -> pd.DataFrame:
    """
    Compare missing-value patterns between pass and fail groups.

    This function is useful for the SECOM dataset because missing values may not
    be random. In semiconductor manufacturing data, missingness can sometimes
    reflect skipped measurements, route differences, sensor/tool availability,
    metrology issues, or abnormal process behavior.

    SECOM target definition:
        -1 = pass
         1 = fail

    Parameters
    ----------
    X : pd.DataFrame
        Feature dataframe. This should contain only process/sensor features.
        Do not include the target column or timestamp column here.

    y : pd.Series
        Target labels aligned with X.
        Expected values:
            -1 = pass
             1 = fail

    Returns
    -------
    pd.DataFrame
        One row per feature with missingness statistics for pass and fail groups.
    """

    # -------------------------------------------------------------------------
    # Safety check:
    # X and y must have the same index so the Boolean masks line up correctly.
    # If the index does not match, the pass/fail filtering may be wrong.
    # -------------------------------------------------------------------------
    assert X.index.equals(y.index), "X and y indexes do not match."

    # Make a copy of y so the function does not accidentally modify the original.
    y = y.copy()

    # -------------------------------------------------------------------------
    # Create Boolean masks for the two target groups.
    #
    # fail_mask is True for rows where the production entity failed.
    # pass_mask is True for rows where the production entity passed.
    # -------------------------------------------------------------------------
    fail_mask = y == 1
    pass_mask = y == -1

    # Count how many passing and failing examples exist.
    # For SECOM, you should expect about 104 failures.
    n_pass = pass_mask.sum()
    n_fail = fail_mask.sum()

    # Optional safety check:
    # Make sure both classes exist before calculating rates.
    if n_pass == 0 or n_fail == 0:
        raise ValueError("Both pass (-1) and fail (1) classes must exist in y.")

    # This list will store one dictionary of results per feature.
    rows = []

    # -------------------------------------------------------------------------
    # Loop through every feature column.
    # For each feature, we calculate how often it is missing in pass rows
    # and how often it is missing in fail rows.
    # -------------------------------------------------------------------------
    for col in X.columns:

        # Boolean Series:
        # True means the value is missing for this feature in that row.
        # False means the value is present.
        missing = X[col].isna()

        # Count missing values among passing examples only.
        pass_missing_count = missing[pass_mask].sum()

        # Count missing values among failing examples only.
        fail_missing_count = missing[fail_mask].sum()

        # Count total missing values for this feature across all rows.
        total_missing_count = missing.sum()

        # Missing rate among passing examples.
        # Example: 100 missing pass rows / 1463 pass rows = 0.068
        pass_missing_rate = pass_missing_count / n_pass

        # Missing rate among failing examples.
        # Example: 30 missing fail rows / 104 fail rows = 0.288
        fail_missing_rate = fail_missing_count / n_fail

        # Difference between fail missing rate and pass missing rate.
        #
        # Positive value:
        #     Feature is missing more often in failed examples.
        #
        # Negative value:
        #     Feature is missing more often in passing examples.
        #
        # Near zero:
        #     Missingness is similar between pass and fail groups.
        missing_rate_diff = fail_missing_rate - pass_missing_rate

        # ---------------------------------------------------------------------
        # Among all rows where this feature is missing,
        # calculate what percentage belong to the failure class.
        #
        # This is useful because SECOM failures are rare.
        # If the general failure rate is about 6.6%, but 40% of rows with this
        # feature missing are failures, then missingness may be informative.
        # ---------------------------------------------------------------------
        if total_missing_count > 0:
            fail_share_among_missing = fail_missing_count / total_missing_count
        else:
            # If the feature is never missing, this value is not applicable.
            fail_share_among_missing = np.nan

        # ---------------------------------------------------------------------
        # Convert Boolean masks to 0/1 so we can compare missingness directly
        # against the failure flag.
        #
        # missing_as_int:
        #     1 = this feature is missing in this row
        #     0 = this feature is not missing
        #
        # fail_as_int:
        #     1 = this row is a failure
        #     0 = this row is not a failure
        # ---------------------------------------------------------------------
        missing_as_int = missing.astype(int)
        fail_as_int = fail_mask.astype(int)

        # Check whether this feature's missingness pattern exactly matches
        # the failure flag.
        #
        # True means:
        #     feature is missing for every failed row
        #     feature is not missing for every passing row
        #
        # This is very suspicious and should be reviewed for possible leakage
        # or data-generation artifacts before using the feature in a model.
        exact_match_fail_flag = missing_as_int.equals(fail_as_int)

        # Check whether every failed example has this feature missing.
        #
        # Important:
        # This does not mean the feature is missing only for failures.
        # It may also be missing for some passing rows.
        all_fails_missing = fail_missing_count == n_fail

        # Check whether missingness occurs only in failed examples.
        #
        # True means:
        #     no passing rows are missing this feature
        #     at least one failed row is missing this feature
        #
        # This can be a strong rare-failure signal, but it still needs review.
        missing_only_when_fail = (
            total_missing_count > 0
            and pass_missing_count == 0
            and fail_missing_count > 0
        )

        # Check whether missingness perfectly separates failures from passes.
        #
        # True means:
        #     all failed rows are missing this feature
        #     no passing rows are missing this feature
        #
        # This is equivalent to a perfect missingness-based failure flag.
        # In real projects, this should be treated carefully because it may
        # indicate leakage, a downstream measurement, or a data artifact.
        perfect_failure_missing_signal = (
            fail_missing_count == n_fail
            and pass_missing_count == 0
        )

        # Store all calculated values for this feature.
        rows.append({
            "feature": col,

            # Dataset-level class counts
            "n_pass": n_pass,
            "n_fail": n_fail,

            # Missing-value counts
            "pass_missing_count": pass_missing_count,
            "fail_missing_count": fail_missing_count,
            "total_missing_count": total_missing_count,

            # Missing-value rates
            "pass_missing_rate": pass_missing_rate,
            "fail_missing_rate": fail_missing_rate,
            "missing_rate_diff_fail_minus_pass": missing_rate_diff,

            # Among missing rows, how many are failures?
            "fail_share_among_missing": fail_share_among_missing,

            # Special missingness pattern flags
            "all_fails_missing": all_fails_missing,
            "missing_only_when_fail": missing_only_when_fail,
            "perfect_failure_missing_signal": perfect_failure_missing_signal,
            "exact_match_fail_flag": exact_match_fail_flag,
        })

    # Convert the list of dictionaries into a dataframe.
    report = pd.DataFrame(rows)

    # -------------------------------------------------------------------------
    # Sort the report so the most important/suspicious features appear first.
    #
    # Priority 1:
    #     Features where missingness perfectly matches the failure label.
    #
    # Priority 2:
    #     Features missing much more often in failures than passes.
    #
    # Priority 3:
    #     Features missing in more failed rows.
    # -------------------------------------------------------------------------
    report = report.sort_values(
        by=[
            "perfect_failure_missing_signal",
            "missing_rate_diff_fail_minus_pass",
            "fail_missing_count",
        ],
        ascending=[False, False, False]
    )

    return report


def create_pipeline(threshold=0.50, 
                    imputer=SimpleImputer(strategy="median"),
                    scaler=StandardScaler(), 
                    classifier=LogisticRegression(class_weight="balanced", max_iter=5000,random_state=42),
                    ):
    
    # -------------------------------------------------------------
    # If use_imputer=True:
    #     Replace missing values using the selected strategy.
    #
    # If use_imputer=False:
    #     Pass the original NaN values directly to the model.
    # -------------------------------------------------------------
    use_imputer = imputer if imputer is not None else "passthrough"

    # -------------------------------------------------------------
    # SCALER STEP
    # -------------------------------------------------------------
    # If scaler=None, skip scaling.
    #
    # This is useful for tree-based models such as
    # HistGradientBoostingClassifier, RandomForest, etc.
    # -------------------------------------------------------------
    scaler_step = scaler if scaler is not None else "passthrough"

    return Pipeline(
        steps=[
            (
                "drop_high_missing",
                DropHighMissingFeatures(threshold=threshold),
            ),
            (
                "imputer",
                use_imputer,
            ),
            (
                "scaler",
                scaler_step,
            ),
            (
                "classifier",
                classifier,
            ),
        ]
)


# ---------------------------------------------------------
# SECOM class labels
# ---------------------------------------------------------
PASS_LABEL = -1
FAIL_LABEL = 1


# ---------------------------------------------------------
# Custom scorers focused on the failure class
# ---------------------------------------------------------
failure_recall = make_scorer(
    recall_score,
    pos_label=FAIL_LABEL,
    zero_division=0
)

failure_precision = make_scorer(
    precision_score,
    pos_label=FAIL_LABEL,
    zero_division=0
)

failure_f1 = make_scorer(
    f1_score,
    pos_label=FAIL_LABEL,
    zero_division=0
)


# ---------------------------------------------------------
# Metrics evaluated during cross-validation
# ---------------------------------------------------------
SCORING = {
    "balanced_accuracy": "balanced_accuracy",
    "failure_recall": failure_recall,
    "failure_precision": failure_precision,
    "failure_f1": failure_f1,
    "average_precision": "average_precision",
}


def evaluate_pipeline_cv(
    pipeline,
    X,
    y,
    pipeline_name="model",
    n_splits=5,
    n_repeats=5,
    random_state=42,
    n_jobs=-1,
):
    """
    Evaluate a classification pipeline using repeated stratified
    cross-validation.

    Designed for the SECOM semiconductor dataset where:

        -1 = pass
         1 = fail

    The function evaluates:
        - balanced accuracy
        - balanced error rate (BER)
        - failure recall
        - false-negative rate (FNR)
        - failure precision
        - failure F1-score
        - average precision

    Parameters
    ----------
    pipeline :
        A scikit-learn estimator or Pipeline.

    X : pd.DataFrame
        Feature matrix.

    y : pd.Series
        Target variable.

    pipeline_name : str
        Name used in the returned summary table.

    n_splits : int, default=5
        Number of folds used in each repetition.

    n_repeats : int, default=5
        Number of times the stratified cross-validation is repeated.

    random_state : int, default=42
        Controls reproducibility of the CV splits.

    n_jobs : int, default=-1
        Number of CPU cores to use.
        -1 uses all available processors.

    Returns
    -------
    summary : pd.DataFrame
        One-row dataframe containing mean and standard deviation
        for each metric.

    raw_scores : dict
        Original results returned by sklearn.cross_validate().
        Useful if you want to inspect individual fold scores.
    """

    # -----------------------------------------------------
    # Basic safety checks
    # -----------------------------------------------------

    # X and y should represent the same rows.
    if len(X) != len(y):
        raise ValueError("X and y must contain the same number of rows.")

    # Make sure both SECOM classes exist.
    unique_labels = set(pd.Series(y).unique())

    expected_labels = {PASS_LABEL, FAIL_LABEL}

    if not expected_labels.issubset(unique_labels):
        raise ValueError(
            f"Expected labels {expected_labels}, "
            f"but found {unique_labels}."
        )

    # -----------------------------------------------------
    # Repeated Stratified K-Fold
    #
    # Stratification attempts to preserve the pass/fail
    # proportion inside every validation fold.
    #
    # This is especially important because SECOM has only
    # 104 failure observations.
    # -----------------------------------------------------
    cv = RepeatedStratifiedKFold(
        n_splits=n_splits,
        n_repeats=n_repeats,
        random_state=random_state,
    )

    # -----------------------------------------------------
    # Run cross-validation
    #
    # Every preprocessing step inside the pipeline is fitted
    # separately on each training fold.
    #
    # This prevents preprocessing leakage from the validation
    # folds into the training process.
    # -----------------------------------------------------
    raw_scores = cross_validate(
        estimator=pipeline,
        X=X,
        y=y,
        cv=cv,
        scoring=SCORING,
        n_jobs=n_jobs,
        return_train_score=False,
        error_score="raise",
    )

    # -----------------------------------------------------
    # Extract the validation scores
    # -----------------------------------------------------
    balanced_accuracy = raw_scores["test_balanced_accuracy"]
    failure_recall_scores = raw_scores["test_failure_recall"]
    failure_precision_scores = raw_scores["test_failure_precision"]
    failure_f1_scores = raw_scores["test_failure_f1"]
    average_precision_scores = raw_scores["test_average_precision"]

    # -----------------------------------------------------
    # Derived manufacturing-relevant metrics
    #
    # BER:
    #   lower is better
    #
    # FNR:
    #   percentage of true failures that were missed
    # -----------------------------------------------------
    ber_scores = 1 - balanced_accuracy

    false_negative_rate_scores = 1 - failure_recall_scores

    # -----------------------------------------------------
    # Create one summary row for this pipeline
    # -----------------------------------------------------
    summary = pd.DataFrame({
        "pipeline": [pipeline_name],

        "balanced_accuracy_mean": [
            balanced_accuracy.mean()
        ],
        "balanced_accuracy_std": [
            balanced_accuracy.std()
        ],

        "ber_mean": [
            ber_scores.mean()
        ],
        "ber_std": [
            ber_scores.std()
        ],

        "failure_recall_mean": [
            failure_recall_scores.mean()
        ],
        "failure_recall_std": [
            failure_recall_scores.std()
        ],

        "false_negative_rate_mean": [
            false_negative_rate_scores.mean()
        ],

        "failure_precision_mean": [
            failure_precision_scores.mean()
        ],
        "failure_precision_std": [
            failure_precision_scores.std()
        ],

        "failure_f1_mean": [
            failure_f1_scores.mean()
        ],
        "failure_f1_std": [
            failure_f1_scores.std()
        ],

        "average_precision_mean": [
            average_precision_scores.mean()
        ],
        "average_precision_std": [
            average_precision_scores.std()
        ],

        "mean_fit_time": [
            raw_scores["fit_time"].mean()
        ],
    })

    return summary, raw_scores


def build_feature_eda_report(
    X: pd.DataFrame,
    y: pd.Series,
    pass_label=-1,
    fail_label=1,
    lower_quantile=0.05,
    upper_quantile=0.95,
) -> pd.DataFrame:
    """
    Create a feature-level EDA report for the SECOM dataset.

    Each row in the returned dataframe represents one feature.

    The report describes:

    1. Overall feature behavior
       - missing rate
       - mean
       - median
       - standard deviation
       - variance
       - min / max
       - skew
       - IQR
       - IQR-based outlier rate
       - number of unique values

    2. Pass vs fail behavior
       - pass mean / median
       - fail mean / median
       - mean difference
       - median difference
       - standardized mean difference

    3. Failure behavior in extreme regions
       - 5th percentile of PASS population
       - 95th percentile of PASS population
       - percentage of FAIL examples outside those limits

    SECOM labels:
        -1 = pass
         1 = fail

    Parameters
    ----------
    X : pd.DataFrame
        Feature matrix. Should contain numerical process/sensor features.

    y : pd.Series
        Target labels aligned with X.

    pass_label : int, default=-1
        Label representing passing examples.

    fail_label : int, default=1
        Label representing failing examples.

    lower_quantile : float, default=0.05
        Lower PASS distribution threshold used for extreme-value analysis.

    upper_quantile : float, default=0.95
        Upper PASS distribution threshold used for extreme-value analysis.

    Returns
    -------
    pd.DataFrame
        One row per feature with EDA statistics.
    """

    # ------------------------------------------------------------------
    # Safety checks
    # ------------------------------------------------------------------

    if len(X) != len(y):
        raise ValueError("X and y must contain the same number of rows.")

    if not X.index.equals(y.index):
        raise ValueError("X and y indexes must match.")

    # Boolean masks identifying PASS and FAIL rows.
    pass_mask = y == pass_label
    fail_mask = y == fail_label

    n_pass = pass_mask.sum()
    n_fail = fail_mask.sum()

    if n_pass == 0 or n_fail == 0:
        raise ValueError(
            "Both pass and fail classes must exist in the target."
        )

    # This will contain one dictionary for every feature.
    rows = []

    # ------------------------------------------------------------------
    # Analyze every feature independently
    # ------------------------------------------------------------------

    for col in X.columns:

        s = X[col]

        # Skip non-numeric columns.
        # Timestamp, for example, should normally be analyzed separately.
        if not pd.api.types.is_numeric_dtype(s):
            continue

        # --------------------------------------------------------------
        # BASIC DATA QUALITY
        # --------------------------------------------------------------

        n_total = len(s)
        n_missing = s.isna().sum()
        missing_rate = n_missing / n_total

        # Values available for analysis.
        observed = s.dropna()

        n_observed = len(observed)
        n_unique = observed.nunique()

        # If the feature contains no observed values, most statistics
        # cannot be calculated.
        if n_observed == 0:
            rows.append({
                "feature": col,
                "n_observed": 0,
                "n_missing": n_missing,
                "missing_rate": missing_rate,
            })
            continue

        # --------------------------------------------------------------
        # OVERALL DISTRIBUTION
        # --------------------------------------------------------------

        mean = observed.mean()
        median = observed.median()
        std = observed.std()
        variance = observed.var()

        minimum = observed.min()
        maximum = observed.max()

        # Skew measures asymmetry.
        #
        # Around 0:
        #     approximately symmetric
        #
        # Strong positive:
        #     long right tail
        #
        # Strong negative:
        #     long left tail
        skew = observed.skew()

        # --------------------------------------------------------------
        # INTERQUARTILE RANGE
        # --------------------------------------------------------------

        q1 = observed.quantile(0.25)
        q3 = observed.quantile(0.75)

        iqr = q3 - q1

        # Standard Tukey outlier boundaries.
        lower_iqr_bound = q1 - (1.5 * iqr)
        upper_iqr_bound = q3 + (1.5 * iqr)

        # --------------------------------------------------------------
        # OUTLIER RATE
        # --------------------------------------------------------------
        #
        # We calculate the percentage of observed values that fall
        # outside the IQR boundaries.
        #
        # Important:
        # An outlier is NOT automatically a bad data point.
        # In semiconductor data, extreme observations may represent
        # process excursions or unusual manufacturing conditions.
        # --------------------------------------------------------------

        if iqr > 0:

            outlier_mask = (
                (observed < lower_iqr_bound)
                | (observed > upper_iqr_bound)
            )

            outlier_count = outlier_mask.sum()

            outlier_rate = (
                outlier_count / n_observed
            )

        else:
            outlier_count = 0
            outlier_rate = 0.0

        # --------------------------------------------------------------
        # SPLIT FEATURE INTO PASS AND FAIL POPULATIONS
        # --------------------------------------------------------------

        pass_values = s[pass_mask].dropna()
        fail_values = s[fail_mask].dropna()

        pass_count = len(pass_values)
        fail_count = len(fail_values)

        # --------------------------------------------------------------
        # PASS DISTRIBUTION
        # --------------------------------------------------------------

        pass_mean = (
            pass_values.mean()
            if pass_count > 0
            else np.nan
        )

        pass_median = (
            pass_values.median()
            if pass_count > 0
            else np.nan
        )

        pass_std = (
            pass_values.std()
            if pass_count > 1
            else np.nan
        )

        # --------------------------------------------------------------
        # FAIL DISTRIBUTION
        # --------------------------------------------------------------

        fail_mean = (
            fail_values.mean()
            if fail_count > 0
            else np.nan
        )

        fail_median = (
            fail_values.median()
            if fail_count > 0
            else np.nan
        )

        fail_std = (
            fail_values.std()
            if fail_count > 1
            else np.nan
        )

        # --------------------------------------------------------------
        # PASS / FAIL DIFFERENCES
        # --------------------------------------------------------------

        mean_difference = fail_mean - pass_mean
        median_difference = fail_median - pass_median

        # --------------------------------------------------------------
        # STANDARDIZED MEAN DIFFERENCE
        #
        # Similar to Cohen's d.
        #
        # This lets us compare features even though their numerical
        # scales may be completely different.
        #
        # Positive:
        #     failures tend to have larger values
        #
        # Negative:
        #     failures tend to have smaller values
        #
        # Large absolute values:
        #     stronger pass/fail separation
        # --------------------------------------------------------------

        if (
            pass_count > 1
            and fail_count > 1
            and not np.isnan(pass_std)
            and not np.isnan(fail_std)
        ):

            pooled_variance = (
                (
                    (pass_count - 1) * pass_std**2
                    + (fail_count - 1) * fail_std**2
                )
                /
                (
                    pass_count
                    + fail_count
                    - 2
                )
            )

            pooled_std = np.sqrt(pooled_variance)

            if pooled_std > 0:
                standardized_mean_difference = (
                    mean_difference / pooled_std
                )
            else:
                standardized_mean_difference = 0.0

        else:
            standardized_mean_difference = np.nan

        # --------------------------------------------------------------
        # FAILURE EXTREME-RANGE ANALYSIS
        #
        # Instead of defining "extreme" using the entire dataset,
        # define NORMAL boundaries using PASS observations.
        #
        # Example:
        #
        # PASS 5th percentile  = 100
        # PASS 95th percentile = 150
        #
        # Then ask:
        #
        # "What percentage of FAIL observations fall below 100
        #  or above 150?"
        #
        # With 5% / 95% boundaries, approximately 10% of PASS
        # observations should naturally lie outside the range.
        #
        # If 30%, 40%, 50%, etc. of failures are outside,
        # that feature becomes interesting.
        # --------------------------------------------------------------

        if pass_count > 0 and fail_count > 0:

            pass_lower_limit = pass_values.quantile(
                lower_quantile
            )

            pass_upper_limit = pass_values.quantile(
                upper_quantile
            )

            fail_extreme_mask = (
                (fail_values < pass_lower_limit)
                | (fail_values > pass_upper_limit)
            )

            fail_extreme_count = fail_extreme_mask.sum()

            fail_extreme_rate = (
                fail_extreme_count / fail_count
            )

            # Separately calculate upper- and lower-tail behavior.
            fail_low_extreme_rate = (
                (fail_values < pass_lower_limit).mean()
            )

            fail_high_extreme_rate = (
                (fail_values > pass_upper_limit).mean()
            )

        else:

            pass_lower_limit = np.nan
            pass_upper_limit = np.nan

            fail_extreme_count = 0
            fail_extreme_rate = np.nan

            fail_low_extreme_rate = np.nan
            fail_high_extreme_rate = np.nan

        # --------------------------------------------------------------
        # STORE RESULTS FOR THIS FEATURE
        # --------------------------------------------------------------

        rows.append({
            "feature": col,

            # Data availability
            "n_observed": n_observed,
            "n_missing": n_missing,
            "missing_rate": missing_rate,
            "n_unique": n_unique,

            # Overall distribution
            "mean": mean,
            "median": median,
            "std": std,
            "variance": variance,
            "min": minimum,
            "max": maximum,
            "skew": skew,

            # Robust spread
            "q1": q1,
            "q3": q3,
            "iqr": iqr,

            # Outliers
            "outlier_count": outlier_count,
            "outlier_rate": outlier_rate,

            # Pass information
            "pass_count": pass_count,
            "pass_mean": pass_mean,
            "pass_median": pass_median,
            "pass_std": pass_std,

            # Failure information
            "fail_count": fail_count,
            "fail_mean": fail_mean,
            "fail_median": fail_median,
            "fail_std": fail_std,

            # Pass/fail comparison
            "mean_difference_fail_minus_pass":
                mean_difference,

            "median_difference_fail_minus_pass":
                median_difference,

            "standardized_mean_difference":
                standardized_mean_difference,

            "abs_standardized_mean_difference":
                abs(standardized_mean_difference)
                if not np.isnan(
                    standardized_mean_difference
                )
                else np.nan,

            # Extreme-range analysis
            "pass_lower_5pct":
                pass_lower_limit,

            "pass_upper_95pct":
                pass_upper_limit,

            "fail_extreme_count":
                fail_extreme_count,

            "fail_extreme_rate":
                fail_extreme_rate,

            "fail_low_extreme_rate":
                fail_low_extreme_rate,

            "fail_high_extreme_rate":
                fail_high_extreme_rate,
        })

    # Convert all feature dictionaries into a dataframe.
    report = pd.DataFrame(rows)

    return report