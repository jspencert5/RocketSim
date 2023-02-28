import math

# Constant in MPH
gravity = 9.81


# Equation for time of flight
def timeOfFlight(v, a):
    a = math.radians(a)
    time = 2 * (v / gravity) * math.sin(a)
    return time


# Equation for horizontal range
def rangeHor(v, a):
    a = math.radians(a)
    distance = ((v * v) * math.sin(a * 2)) / gravity
    return distance


# Equation for maximum height
def maxHeight(v, a):
    a = math.radians(a)
    height = ((v*math.sin(a))*(v*math.sin(a)) / (2 * gravity))
    return height


# Equation for x position
def xPos(v, a, x):
    posList = []
    a = math.radians(a)

    for i in x:
        pos = v * math.cos(a) * i
        posList.append(pos)

    return posList


# Equation for y position
def yPos(v, a, y):
    posList = []
    a = math.radians(a)

    for i in y:
        pos = (v * math.sin(a) * i) - (.5 * gravity * (i*i))
        posList.append(pos)

    return posList
