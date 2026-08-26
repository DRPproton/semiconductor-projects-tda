from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd

class DropHighMissingFeatures(BaseEstimator, TransformerMixin):
    """
    Remove features whose missing-value rate exceeds a selected threshold.
    """
    def __init__(self, threshold=0.5):
        # ONLY hyperparameters belong here. 
        # Do not initialize learned attributes (like features_to_drop) here.
        self.threshold = threshold

    def fit(self, X : pd.DataFrame, y = None):
        if not isinstance(X, pd.DataFrame):
            raise ValueError("DropHighMissingFeatures expects a pandas DataFrame.")

        # Learned attributes get a trailing underscore (_)
        self.missing_rate_ = X.isnull().mean()

        self.features_to_drop_ = self.missing_rate_[self.missing_rate_ > self.threshold].index.tolist()
        self.features_to_keep_ = self.missing_rate_[self.missing_rate_ <= self.threshold].index.tolist()

        return self

    def transform(self, X : pd.DataFrame) -> pd.DataFrame:
        if not isinstance(X, pd.DataFrame):
            raise ValueError("DropHighMissingFeatures expects a pandas DataFrame.")

        # Use the learned attribute with the underscore
        return X.drop(columns=self.features_to_drop_, errors='ignore').copy()

    def get_features_to_drop_and_keep(self) -> dict:
        # Optional helper method
        return {
            'features_to_drop': getattr(self, 'features_to_drop_', None), 
            'features_to_keep': getattr(self, 'features_to_keep_', None)
        }
        
        
class DropCorrelatedFeatures(BaseEstimator, TransformerMixin):
    """
    Remove highly correlated numerical features.

    Among correlated features, preference is given to the feature
    with the lower missing-value rate.
    """

    def __init__(
        self,
        threshold=0.90,
        method="spearman",
        min_periods=100
    ):
        self.threshold = threshold
        self.method = method
        self.min_periods = min_periods

    def fit(self, X: pd.DataFrame, y=None):
        if not isinstance(X, pd.DataFrame):
            raise ValueError(
                "DropCorrelatedFeatures expects a pandas DataFrame."
            )

        if not 0 < self.threshold <= 1:
            raise ValueError(
                "threshold must be greater than 0 and at most 1."
            )

        if self.method not in {"spearman", "pearson"}:
            raise ValueError(
                "method must be 'spearman' or 'pearson'."
            )

        missing_rates = X.isna().mean()

        correlation_matrix = X.corr(
            method=self.method,
            min_periods=self.min_periods
        ).abs()

        # Stable sorting means ties preserve the original column order.
        features_by_priority = sorted(
            X.columns,
            key=lambda feature: missing_rates[feature]
        )

        retained_by_priority = []
        dropped_relationships = []

        for feature in features_by_priority:
            correlated_retained_features = [
                retained_feature
                for retained_feature in retained_by_priority
                if (
                    pd.notna(
                        correlation_matrix.loc[
                            feature,
                            retained_feature
                        ]
                    )
                    and correlation_matrix.loc[
                        feature,
                        retained_feature
                    ] >= self.threshold
                )
            ]

            if correlated_retained_features:
                representative = max(
                    correlated_retained_features,
                    key=lambda retained_feature:
                        correlation_matrix.loc[
                            feature,
                            retained_feature
                        ]
                )

                dropped_relationships.append({
                    "dropped_feature": feature,
                    "retained_feature": representative,
                    "absolute_correlation":
                        correlation_matrix.loc[
                            feature,
                            representative
                        ],
                    "dropped_missing_rate":
                        missing_rates[feature],
                    "retained_missing_rate":
                        missing_rates[representative],
                })
            else:
                retained_by_priority.append(feature)

        retained_set = set(retained_by_priority)

        # Return retained columns in their original dataframe order.
        self.features_to_keep_ = [
            feature
            for feature in X.columns
            if feature in retained_set
        ]

        self.features_to_drop_ = [
            feature
            for feature in X.columns
            if feature not in retained_set
        ]

        self.dropped_relationships_ = pd.DataFrame(
            dropped_relationships
        )

        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        if not isinstance(X, pd.DataFrame):
            raise ValueError(
                "DropCorrelatedFeatures expects a pandas DataFrame."
            )

        missing_columns = [
            feature
            for feature in self.features_to_keep_
            if feature not in X.columns
        ]

        if missing_columns:
            raise ValueError(
                f"Required columns are missing: {missing_columns}"
            )

        return X.loc[:, self.features_to_keep_].copy()

    def get_features_to_drop_and_keep(self):
        return {
            "features_to_drop":
                getattr(self, "features_to_drop_", None),
            "features_to_keep":
                getattr(self, "features_to_keep_", None),
        }