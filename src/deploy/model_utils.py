# Importing the libraries
import numpy as np
import joblib


class CycleTransformer:
    """Creates 2 new columns to represent cyclic data.
    Applies sine and cosine function to the original column
    """

    def __init__(self, column_idxs, num_unique_list):
        """Initializes the CycleTransformer object.

        Args:
            column_idxs (list): list of column indicies which to transform
            num_unique (list[int]): list containing the number of unique values that each feature can have
        """
        self.num_unique_list = num_unique_list
        self.column_idxs = column_idxs

    def fit(self):
        return self

    def fit_transform(self, X, y=None):
        """Calls the `transform` method

        Args:
            X (np.ndarray): 2D numpy array containing the data in rows and columns.
            y (list, optional): list or numpy array containing the corresponding labels. Defaults to None.

        Returns:
            _type_: _description_
        """
        return self.transform(X, y)

    def transform(self, X, y=None):
        """Creates 2 new columns, drops the original column

        Args:
            X (np.ndarray): 2D numpy array containing the data in rows and columns.
            y (list, optional): list or numpy array containing the corresponding labels. Defaults to None.
        """

        X_new = X.copy()
        X_new = np.delete(X_new, self.column_idxs, axis=1)

        for column_idx, num_unique in zip(self.column_idxs, self.num_unique_list):
            new_sin_feature = np.sin(
                2 * np.pi * X[:, column_idx] / num_unique).reshape(-1, 1)
            new_cos_feature = np.cos(
                2 * np.pi * X[:, column_idx] / num_unique).reshape(-1, 1)
            X_new = np.append(X_new, new_sin_feature, axis=1)
            X_new = np.append(X_new, new_cos_feature, axis=1)
        return X_new


def load_model_pipeline(filename):
    """Loads a model or pipeline from a file.

    Args:
        filename (str): path to model

    Returns:
        _type_: loaded model
    """
    return joblib.load(filename)
