import math
import matplotlib.pyplot as plt
import numpy as np


# Constant in MPH
gravity = 21.937


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

    for i in x:
        pos = (v * math.sin(a) * i) - (.5 * gravity * (i*i))
        posList.append(pos)

    return posList


# ------------------------------------------------------------------------------------------------
# Take in user input
velocity = float(input("Enter initial velocity: "))
angle = float(input("Enter angle of launch: "))

# Calculate important values
time = timeOfFlight(velocity, angle)
height = maxHeight(velocity, angle)
distance = rangeHor(velocity, angle)

# Generate range that from 0 to time of flight containing ~30 data points per second
x = np.linspace(0.0, time, num=int(time*30))

# Create list of x and y coordinates at resolution = time
xPosList = xPos(velocity, angle, x)
yPosList = yPos(velocity, angle, x)

# Print important values
print("--IMPORTANT VALUES--")
print("Time of flight: {}".format(time))
print("Maximum height reached: {}".format(height))
print("Horizontal distance covered: {}".format(distance))

# Plot graph
plt.plot(xPosList, yPosList)
plt.show()
