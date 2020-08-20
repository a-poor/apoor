"""
apoor.__init__.py
created by Austin Poor
"""

# Version string
__version__ = "1.1.1"



# Standard library imports
import itertools as it

# External library imports
import numpy as np

# Internal module imports
from . import data




def set_seed(n):
    """
    Sets numpy's random seed to `n`.
    """
    np.random.seed(n)


def make_scale(dmin,dmax,rmin,rmax,clamp=False):
    """
    Creates a scale function to map a number from
    a domain to a range.

    Inputs:
        dmin, dmax: numeric start and end values
            for the domain
        rmin, rmax: numeric start and end values
            for the range
        clamp: if the value is outside the range,
            return clamped value (default: False)
    Outputs:
        scale: function taking one numeric argument
            and returns the value mapped from the
            domain to the range (and clamped if
            `clamp` flag is set).

    Examples:
        >>> s = make_scale(0,1,0,10)
        >>> s(0.1)
        1.0

        >>> s = make_scale(0,10,10,0)
        >>> s(1.0)
        9.0

        >>> s = make_scale(0,1,0,1,clamp=True)
        >>> s(100)
        1.0
    """
    drange = dmax - dmin
    rrange = rmax - rmin
    scale_factor = rrange / drange
    def scale(n):
        n_ = (n - dmin) * scale_factor + rmin
        if clamp: return min(max(n_,rmin),rmax)
        else: return n_ 
    return scale
    

def train_test_split(*arrays,test_pct=0.15,val_set=False,val_pct=0.15):
    """
    Splits arrays into train, test, and (optionally) 
    validation sets using the supplied percentages.

    Inputs:
        *arrays: 
            An arbitrary number of sequences to be split
            into train, test, and (optionally) validation 
            sets. Must have at least one array.

        test_pct: float of the range [0,1] (default `0.15`)
            Percent of total n values to include in test set.
            
            The train set will have `1.0 - test_pct` pct of
            values (or `1.0 - test_pct - val_pct` pct of values
            if `val_set == True`).

        val_set: bool (default `False`) 
            Whether or not to return a validation set,
            in addition to a test set.

        val_pct: float of the range [0,1] (default `0.15`)
            Percent of total n values to include in test set.
            
            Ignored if `val_set == False`.
            
            The train set will have `1.0 - test_pct - val_pct` 
            pct of values.

    Outputs:
        splits: tuple of numpy arrays
        Input arrays split into train, test, val sets.
        
        If `val_set == False`, `len(splits) == 2 * len(arrays)`,
        or if `val_set == True`, `len(splits) == 3 * len(arrays)`.

    Examples:
        >>> x = np.arange(10)
        >>> train_test_split(x)
        (array([3, 9, 4, 2, 1, 0, 7, 5, 8]), array([6]))

        >>> x = np.arange(10)
        >>> y = x[::-1]
        >>> x_train, x_test, y_train, y_test = train_test_split(x,y)
        >>> x_train, x_test, y_train, y_test
        (array([1, 3, 5, 8, 4, 7, 6, 9]),
         array([0, 2]),
         array([8, 6, 4, 1, 5, 2, 3, 0]),
         array([9, 7]))

        >>> train_test_split(x,test_pct=0.3,val_set=True,val_pct=0.2)
        (array([0, 9, 5, 7, 6, 2, 8]), 
         array([1, 3, 4]), 
         array([3, 4]))

    """
    # Perform input checks
    assert arrays, "No arrays supplied"
    lens = [len(a) for a in arrays]
    assert len(set(lens)) == 1, "arrays have varying lengths"
    assert lens[0] > 0, "supplied arrays have `len == 0`"
    if val_set:
        assert 0.0 <= test_pct <= 1.0, "`test_pct` must be in the range `0.0 <= test_pct <= 1.0`"
        assert 0.0 <= val_pct <= 1.0, "`val_pct` must be in the range `0.0 <= val_pct <= 1.0`"
        assert test_pct + val_pct <= 1.0, "Can't have `test_pc + val_pct >= 1.0`"
    else:
        assert 0.0 <= test_pct <= 1.0, "`test_pct` must be in the range `0.0 <= test_pct <= 1.0`"
        assert test_pct <= 1.0, "Can't have `test_pc >= 1.0`"
    # Calculate lengths
    n = lens[0]
    n_test = int(n * test_pct)
    # Shuffle the indexes
    indexes = np.arange(n)
    np.random.shuffle(indexes)
    # Split the data
    if val_set:
        n_val = int(n * val_pct)
        n_train = n - n_test - n_val
        splits = (
            (
                a[indexes[:n_train]], 
                a[indexes[n_train:n_train+n_test]], 
                a[indexes[-n_val:]]
            )
            for a in map(np.asarray,arrays)
        )
    else:
        n_train = n - n_test
        splits = (
            (a[indexes[:n_train]], a[indexes[n_train:]])
            for a in map(np.asarray,arrays)
        )
    return tuple(it.chain(*splits))

