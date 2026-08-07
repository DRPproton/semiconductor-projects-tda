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