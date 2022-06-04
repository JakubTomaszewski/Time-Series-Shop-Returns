# Importing the libraries
import numpy as np
import joblib
import requests
import json


def load_model_pipeline(filename):
    """Loads a model or pipeline from a file.

    Args:
        filename (str): path to model

    Returns:
        _type_: loaded model
    """
    return joblib.load(filename)
