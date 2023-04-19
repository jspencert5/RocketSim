"""

Kinematics
Desc: methods to calculate the kinematics of the rocket


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
    vx, vy, vz = v
    dpx = vx * dt
    dpy = vy * dt
    dpz = vz * dt
    return [dpx, dpy, dpz]


def calcDV(a, dt):
    """
    calcDV
    Desc: calculates the change in velocity based on the change in time and acceleration (dv = a * dt)
    Params:
        a: acceleration [x,y,z] m/s^2
        dt: change in time, s
    Returns: [dvx, dvy, dvz]
    """
    ax, ay, az = a
    dvx = ax * dt
    dvy = ay * dt
    dvz = az * dt
    return [dvx, dvy, dvz]


def calcAcceleration(F, m):
    """
    calcAcceleration
    Desc: calculates the acceleration based on the current forces and mass (a = F / m)
    Params:
        F: force in newtons, [x,y,z]
        m: mass, in grams
    Returns: array [ax, ay, az]
    """
    Fx, Fy, Fz = F
    ax = Fx / m
    ay = Fy / m
    az = Fz / m
    return [ax, ay, az]


def calcDM(dt, thrust, v):
    """
    
    """

    return 0
