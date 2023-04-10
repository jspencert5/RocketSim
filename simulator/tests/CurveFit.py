
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



from osim.database.Database import Parts
from osim.calculations.helpers.misc import fitThrust

db = Parts()

eng = db.getEngine("Estes E12")

import matplotlib.pyplot as plt
import numpy as np

times, thrusts = db.getProfile(eng.profileName)

fitFunc = fitThrust(times, thrusts) # create fit function
print(fitFunc(1)) # value of function at 1

# Demo Plot
plt.plot(times, fitFunc(times), 'g', lw=3)
plt.show()


def getfitFunc():
    return fitFunc
