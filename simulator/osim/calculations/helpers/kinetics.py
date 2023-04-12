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


def calcFNet(drag, gravity, thrust, angle):
    """
    calcFNet
    Desc: combines forces to calculate the net force
    Params:
        drag: force of drag
        gravity: force of gravity [x,y,z]
        thrust: force of thrust
        angle: launch angle of rocket
    Returns: FNet [x,y,z]
    """

    FNet = [0, 0, 0]

    thrustAdj = thrust - drag

    # Finding components of thrust -----
    xThrust = math.cos(angle) * thrustAdj
    yThrust = math.sin(angle) * thrustAdj
    zThrust = math.cos(math.radians(90)) * thrustAdj

    # Forces on x-axis
    FNet[0] = gravity[0] + xThrust

    # Forces on y-axis
    FNet[1] = gravity[1] + yThrust

    # Force of z-axis
    FNet[2] = gravity[2] + zThrust


    # Used for testing -----
    #print(FNet)
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
    #print(drag)
    # ----------------------

    return drag


def calcGravity(mass):
    """
    calcGravity
    Desc: calculates current gravity
    Params:
        mass: mass of rocket, in kg
    Returns: Force of gravity [x,y,z], in m/s^2
    """

    gravity = -1 * (9.81 * mass)

    # Used for testing -----
    #print(gravity)
    # ----------------------

    return [0, gravity, 0]


def calcThrust(time, fitFunction):
    """
    calcThrust
    Desc: calculates current thrust
    Params:
        time: time elapsed since start of ignition of booster
    Returns: Magnitude of the force of thrust, in N
    """

    thrust = fitFunction(time)

    # Used for testing -----
    #print(thrust)
    # ----------------------

    return thrust if (thrust > 0) else 0
