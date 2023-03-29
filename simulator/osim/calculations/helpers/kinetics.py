import math
from math import pi

"""
Kinetics
Desc: methods to calculate the Kinetics of the rocket
"""

# Constants -------------------------------------

# Coefficient of drag, unitless
Cd = .75

# Density of air at sea level, kg/m^3
density = 1.229

# Cross sectional area of nose (each nose has same radius) using pi*r^2, m^2
area = (pi * (12*12)) * .000001

# -----------------------------------------------


def calcFNet(drag, gravity, thrust):
    """
    calcFNet
    Desc: combines forces to calculate the net force
    Params:
        drag: force of drag [x,y,z]
        gravity: force of gravity [x,y,z]
        thrust: force of thrust [x,y,z]
    Returns: FNet [x,y,z]
    """

    FNet = [0, 0, 0]

    # Forces on x-axis
    FNet[0] = drag[0] + gravity[0] + thrust[0]

    # Forces on y-axis
    FNet[1] = drag[1] + gravity[1] + thrust[1]

    # Force of z-axis
    FNet[2] = drag[2] + gravity[2] + thrust[2]


    # Used for testing -----
    print(FNet)
    # ----------------------

    return FNet


def calcDrag(velocity):
    """
    calcDrag
    Desc: calculates current drag
    Params:
        velocity: current velocity of the rocket, in m/s [x, y, z]
        
    Returns: Magnitude of the force of drag, which acts in the opposite direction of thrust, in N
    """

    # Finding complete velocity vector
    dragVector = 0
    for i in range(len(velocity)):
        dragVector += velocity[i] ** 2

    dragVector = math.sqrt(dragVector)

    # Drag calc for complete velocity vector
    drag = .5 * density * (dragVector ** 2) * area * Cd


    # Used for testing -----
    print(drag)
    # ----------------------

    return drag


def calcGravity(mass):
    """
    calcGravity
    Desc: calculates current gravity
    Params:
        mass: mass of rocket, in kg
    Returns: Force of gravity [x,y,z], in m/s
    """

    gravity = 9.81 * mass


    # Used for testing -----
    print(gravity)
    # ----------------------

    return [0, gravity, 0]


def calcThrust():
    """
    calcThrust
    Desc: calculates current thrust
    Params:
        
    Returns: Force of thrust [x,y,z]
    """
    pass