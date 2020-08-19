"""
apoor.__init__.py
created by Austin Poor
"""

def import_():
    global np
    global pd
    global plt
    global sns
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    sns.set()

def make_scale(dmin,dmax,rmin,rmax,clamp=False):
    drange = dmax - dmin
    rrange = rmax - rmin
    scale_factor = rrange / drange
    def scale(n):
        n_ = (n - dmin) * scale_factor + rmin
        if clamp: return min(max(n_,rmin),rmax)
        else: return n_ 
    return scale
    


