import numpy as np
import math

gravity = 21.937


# Equation for time of flight
def timeOfFlight(velocity, angle):
    time = ((2 * velocity) * math.sin(angle)) / gravity
    return time


# Equation for horizontal range
def rangeHor(velocity, angle):
    distance = ((velocity * velocity) *  math.sin(angle * 2)) / gravity
    return distance


# Equation for maximum height
def maxHeight(velocity, angle):
    height = ((velocity * velocity) * (math.sin(angle) * math.sin(angle))) / (2 * gravity)
    return height


# Equation of trajectory
