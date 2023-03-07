import math

# Constant in M/s
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
def xPos(v, a, t):
    posList = []
    a = math.radians(a)

    for i in t:
        pos = v * math.cos(a) * i
        posList.append(pos)

    return posList


# Equation for y position
def yPos(v, a, t):
    posList = []
    a = math.radians(a)

    for i in t:
        pos = (v * math.sin(a) * i) - (.5 * gravity * (i*i))
        posList.append(pos)

    return posList


# Equation for x velocity
def xVelo(v, t):
    veloList = []

    for i in t:
        velo = v
        veloList.append(velo)

    return veloList


# Equation for y velocity
def yVelo(v, t):
    veloList = []

    for i in t:
        velo = (v - (gravity * i))
        veloList.append(velo)

    return veloList


# Equation for x acceleration
def xAcc(t):
    accList = []

    for i in t:
        acc = 0
        accList.append(acc)

    return accList


# Equation for y acceleration
def yAcc(t):
    accList = []

    for i in t:
        acc = gravity * -1
        accList.append(acc)

    return accList
