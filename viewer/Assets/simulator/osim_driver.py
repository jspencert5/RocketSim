from simulator.osim.database.Database import Parts
from simulator.osim.calculations.helpers.kinetics import calcFNet, calcDrag, calcGravity, calcThrust
from simulator.osim.io import io
from simulator.osim.calculations.RocketState import RocketState
from simulator.osim.calculations.helpers.misc import fitThrust

import matplotlib.pyplot as plt

"""

OSIM
Desc: This is the main driver file for the program


"""
def run():

    db = Parts()
    # get input data using i/o
    # fetch needed data using database for parts
    angle, engine, body, nose = io.getSystemArg(db)

    #init rocket state
    rocketState = RocketState()

    # inital params
    # pass variables to run driver function
    rocketState.theta = angle
    rocketState.mP = engine.fuelMass / 1000
    rocketState.mR = (engine.mass + body.mass + nose.mass) / 1000
    rocketState.p = [0,0.1,0] # set position to ~4in off ground 
    rocketState.dt = 1 / 30 # change in time (dt) 1/30 -> 30 frames per second

    times, thrusts = db.getProfile(engine.profileName)
    fitFunc = fitThrust(times, thrusts) # create fit function
    #print(rocketState.mR)
    #plt.plot(times, fitFunc(times), 'g', lw=3)
    #plt.show()

    lines = []

    while(rocketState.p[1] > 0):
        if (rocketState.t <= engine.maxBurnTime):

            # under thrust calcuation goes here

            drag = calcDrag(rocketState.v)
            gravity = calcGravity(rocketState.mR)
            thrust = calcThrust(rocketState.t, fitFunc)

            #print(drag, gravity, thrust)

            netForce = calcFNet(drag, gravity, thrust, rocketState.theta)

            #print(netForce)

            rocketState.updateState(netForce, thrust)

            print(rocketState.v)

            lines.append(rocketState.export())

        else:
            # projectile motion calculation happens here
            break
            lines.append([]) # append project motion data

    # save data
    io.exportSimData(lines, "simulationData.csv")