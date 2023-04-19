
from operator import add
from simulator.osim.calculations.helpers.kinematics import calcDM, calcAcceleration, calcDV, calcDP


class RocketState:
    """
    
    RocketState
    Desc: Holds the current state for the simulation
    Author: Spencer Taintor (N01432549)
    Last Modified: 3/14/23
    
    """

    def __init__(self) -> None:

        # Setting Instance Variables

        self.a = [0,0,0] # current acceleration [x,y,z], m/s^2
        self.v = [0,0,0] # current velocity [x,y,z], m/s
        self.p = [0,0,0] # current position [x,y,z], m

        self.fNet = [0.00001,0,0] # current net force [x,y,z], N
        self.theta = 0 # current angle off of x-axis, rad
        self.mR = 0 # mass rocket
        self.mP = 0 # mass propelent

        self._cd = 0.75 # drag coefficient
        self._P = 1.229 # air density, kg/m^3
        self.dt = 0 #  change in time
        self.t = 0 # current time elapsed, t

    def export(self):
        """
        export
        Desc: returns current state as an array
        """

        return [self.t] + self.p + self.v + self.a + [self.mR]
    
    def updateState(self, fNet, thrust):
        """
        updateState
        Desc:
        """
        
        self.fNet = fNet # update net forces

        self.updateAcceleration(calcAcceleration(fNet, self.mR))
        self.updateVelocity(calcDV(self.a, self.dt))
        self.updatePosition(calcDP(self.v, self.dt))
        self.updateMass(calcDM(self.dt, thrust, self.v))

        self.updateTime(self.dt)


    def updateTime(self, dt):
        """
        updateTime
        Desc: updates current elapsed time based on change in time (tf = ti + dt)
        """
        self.t = self.t + dt

    def updateVelocity(self, dv):
        """
        updateVelocity
        Desc: updates velocity based on change in velocity (vf = vi + dv )
        """
        self.v = list(map(add, self.v, dv))

    def updateAcceleration(self, a):
        """
        updateAcceleration
        Desc: updates acceleration based on change in acceleration (vf = vi + dv )
        """
        self.a = a

    def updatePosition(self, dp):
        """
        updatePosition
        Desc: updates velocity based on change in position (vf = vi + dv )
        """
        self.p = list(map(add, self.p, dp))

    def updateMass(self, dm):
        """
        updateMass
        Desc: updates mass based on change in time (mf = mi - dm )
        """

        self.mR = self.mR + dm



