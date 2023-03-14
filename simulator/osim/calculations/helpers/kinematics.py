"""

Kinematics
Desc: methods to calulcate the kinematics of the rocket


"""

def calcDP(v, dt):
    """
    calcDP
    Desc: calculates the change in position based on the change in time and velocity (dp = v * dt)
    Params:
        velocity: total current velocity
        dt: change in time
    Returns: [dpx, dpy, dpz]
    """
    pass

def calcDV(a, dt):
    """
    calcDV
    Desc: calculates the change in velocity based on the change in time and acceleration (dv = a * dt)
    Params:
        a: acceleration [x,y,z] m/s^2
        dt: change in time, s
    Returns: [dvx, dvy, dvz]
    """
    pass

def calcAcceleration(F, m):
    """
    calcAcceleration
    Desc: calculates the acceleration based on the current forces and mass (a = F / m)
    Params:
        F: force in newtons, [x,y,z]
        m: mass, in grams [x,y,z]
    Returns: array [ax, ay, az]
    """
    pass
