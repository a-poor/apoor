"""
apoor.__init__.py
created by Austin Poor
"""

__version__ = "1.0.0"


def import_(verbose=True):
    """
    imports numpy, pandas, pyplot,
    and seaborn (and calls sns.set())
    and adds them to the global namespace.

    if `verbose` is True, prints the import
    statements.
    """
    global np
    global pd
    global plt
    global sns
    if verbose:
        print(
        "import numpy as np\n"
        "import pandas as pd\n"
        "import matplotlib.pyplot as plt\n"
        "import seaborn as sns\n"
        "sns.set()"
        )
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    sns.set()

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
    


