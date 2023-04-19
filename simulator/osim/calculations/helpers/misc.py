
import numpy as np
from scipy.interpolate import UnivariateSpline

"""

Misc
Desc: helper methods that did not fit the other categories


"""

def fitThrust(xPoints ,yPoints):
    """
    fitThrust
    Desc: creates a fit of the thrust curve using thrustCurveFunction and scipy curve_fit
    """
    print(xPoints ,yPoints)
    return UnivariateSpline(np.asarray(xPoints), np.asarray(yPoints))