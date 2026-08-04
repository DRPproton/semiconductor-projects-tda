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
