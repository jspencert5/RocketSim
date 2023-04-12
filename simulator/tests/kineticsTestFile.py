# File used to test IO for kinetics methods

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



from osim.calculations.helpers.kinetics import calcFNet
from osim.calculations.helpers.kinetics import calcDrag
from osim.calculations.helpers.kinetics import calcGravity

'''
# -----------------------------------------------
drag = []
x = float(input("Enter drag x value: "))
y = float(input("Enter drag y value: "))
z = float(input("Enter drag z value: "))

drag.append(x)
drag.append(y)
drag.append(z)

# -----------------------------------------------
gravity = []
x = float(input("Enter gravity x value: "))
y = float(input("Enter gravity y value: "))
z = float(input("Enter gravity z value: "))

gravity.append(x)
gravity.append(y)
gravity.append(z)

# -----------------------------------------------
thrust = []
x = float(input("Enter thrust x value: "))
y = float(input("Enter thrust y value: "))
z = float(input("Enter thrust z value: "))

thrust.append(x)
thrust.append(y)
thrust.append(z)

# -----------------------------------------------
'''


# to test, comment out line 4 of kinetics file
velocity = [10, 10, 0]

drag = calcDrag(velocity)
gravity = calcGravity(.1)
thrust = 20

calcFNet(drag, gravity, thrust, 45)



