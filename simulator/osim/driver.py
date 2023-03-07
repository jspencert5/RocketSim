import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import mathFunctions
import pandas


# ------------------------------------------------------------------------------------------------
# Take in user input
velocity = float(input("Enter initial velocity: "))
angle = float(input("Enter angle of launch: "))

# Calculate important values
time = mathFunctions.timeOfFlight(velocity, angle)
height = mathFunctions.maxHeight(velocity, angle)
distance = mathFunctions.rangeHor(velocity, angle)

# Generate range that from 0 to time of flight containing ~30 data points per second
t = np.linspace(0.0, time, num=int(time*30))

# Create list of all variables at resolution = time*30
xPosList = mathFunctions.xPos(velocity, angle, t)
yPosList = mathFunctions.yPos(velocity, angle, t)
xVeloList = mathFunctions.xVelo(velocity, t)
yVeloList = mathFunctions.yVelo(velocity, t)
xAccList = mathFunctions.xAcc(t)
yAccList = mathFunctions.yAcc(t)

# Print important values
print("--IMPORTANT VALUES--")
print("Time of flight: {}".format(time))
print("Maximum height reached: {}".format(height))
print("Horizontal distance covered: {}".format(distance))


# Plot graph
plt.plot(xPosList, yPosList)
plt.show()


# Print to CSV
data = {
    'time': t,
    'xPos': xPosList,
    'yPos': yPosList,
    'xVelo': xVeloList,
    'yVelo': yVeloList,
    'xAcc': xAccList,
    'yAcc': yAccList
}

df = pd.DataFrame(data)
df.to_csv('values.csv', index=False)
