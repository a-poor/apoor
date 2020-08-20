"""
apoor.data.__init__.py
created by Austin Poor
"""

import io
import gzip
import pkgutil

import pandas as pd

_datasets = [
    "iris",
    "boston"
]

def _decompress(bstr):
    """
    Helper function for decompressing
    a gzip-ed CSV dataset and converting
    it to a pandas DataFrame.

    Inputs:
        bstr: Binary string of a CSV with 
            gzip compression. 
    Outputs:
        df: pandas DataFrame
    """
    decomp = gzip.decompress(bstr).decode()
    f = io.StringIO(decomp)
    return pd.read_csv(f,encoding="utf-8")

def list_datasets():
    """
    Returns a list of the available datasets.
    
    Each dataset in the list can be loaded
    with a load_<name> function, where
    <name> is the name of the dataset.
    """
    return _datasets[:]

def load_iris():
    """
    Loads the iris dataset as a Pandas
    DataFrame.
    """
    compressed = pkgutil.get_data('apoor.data', '_data/iris.csv.gz')
    df = _decompress(compressed)
    df["target"] = df["target"].astype("category")
    return df

def load_boston():
    """
    Loads the boston housing dataset as a Pandas
    DataFrame.
    """
    compressed = pkgutil.get_data('apoor.data', '_data/boston.csv.gz')
    df = _decompress(compressed)
    df.CHAS = df.CHAS.astype("int8")
    df.MEDV = df.MEDV.astype("int32")
    return df


