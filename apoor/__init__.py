"""
apoor.__init__.py
created by Austin Poor
"""

__version__ = "1.0.2"


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
    Returns:
        scale: function taking one numeric argument
            and returns the value mapped from the
            domain to the range (and clamped if
            `clamp` flag is set).
    """
    drange = dmax - dmin
    rrange = rmax - rmin
    scale_factor = rrange / drange
    def scale(n):
        n_ = (n - dmin) * scale_factor + rmin
        if clamp: return min(max(n_,rmin),rmax)
        else: return n_ 
    return scale
    


