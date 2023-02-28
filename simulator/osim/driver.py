import matplotlib.pyplot as plt
import numpy as np
import mathFunctions


# ------------------------------------------------------------------------------------------------
# Take in user input
velocity = float(input("Enter initial velocity: "))
angle = float(input("Enter angle of launch: "))

# Calculate important values
time = mathFunctions.timeOfFlight(velocity, angle)
height = mathFunctions.maxHeight(velocity, angle)
distance = mathFunctions.rangeHor(velocity, angle)

# Generate range that from 0 to time of flight containing ~30 data points per second
x = np.linspace(0.0, time, num=int(time*30))

# Create list of x and y coordinates at resolution = time
xPosList = mathFunctions.xPos(velocity, angle, x)
yPosList = mathFunctions.yPos(velocity, angle, x)

# Print important values
print("--IMPORTANT VALUES--")
print("Time of flight: {}".format(time))
print("Maximum height reached: {}".format(height))
print("Horizontal distance covered: {}".format(distance))


# Plot graph
plt.plot(xPosList, yPosList)
plt.show()
