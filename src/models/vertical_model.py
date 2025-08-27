# we will define a linear model with current state being [h, v] (height and velocity at some time t) and control input just be u = a (acceleation commanded at time t)

# we will also have some basic constraints that include max and min velocity and acceleration

from typing import Dict, Iterable, Tuple
import numpy as np

#conversion helpers
FT_MIN_TO_FT_SEC = 1.0 / 60.0
FT_SEC_TO_FT_MIN = 60.0

#some really basic constraints 
DEFAULT_CONSTRAINTS = {
    "vz_min": 0.0,    # min vertical speed (ft/s) — pure climb only
    "vz_max": 50.0,   # max vertical speed (ft/s) — 3000 fpm
    "az_min": -0.5,   # min vertical acceleration (ft/s^2)
    "az_max": 0.5,    # max vertical acceleration (ft/s^2)
}

#we have the option to override our past contrants in case we don't want them, since the contraints are in a dict the overriding has to be dict
def constraints(overrides=None):
    c = DEFAULT_CONSTRAINTS.copy()
    if overrides:
        c.update(overrides)
    return c


#our matrices only make sense for positive time obv/ defined some very basic matrices for linear model: its just basic physics here
#does look better on paper or latex
def dynamics_matrices(dt):
    if dt <= 0:
        raise ValueError("dt must be positive")
    A = [[1.0, dt], [0.0, 1.0]]
    B = [[0.5 * dt * dt], [dt]]


#lets make sure that our commanded acceleration does not got below our minimum set in contrants. really simple way to enfornce this contranint
def clip_input(az, c):
    return max(c["az_min"], min(az, c["az_max"]))

#similar logic got the state contraints and check
def clip_state(h, vz, c):
    vz = max(c["vz_min"], min(vz, c["vz_max"]))
    return h, vz

#now lets simulate our step to test out the logic
def simulate_step(h, vz, az, dt, c=None, clip=True):
    if dt <= 0:
        raise ValueError("dt must be positive")
        
    c = constraints() if c is None else c # defining new contraints if any but contraints is set to optional 
    
    if clip: 
        az = clip_input(az, c) #always make sure to clip to stay within constraints
        
    vz_next = vz + az * dt
    h_next = h + vz * dt + 0.5 * az * dt * dt
    
    if clip:
        return clip_state(h_next, vz_next, c) #staying within contraints
    return h_next, vz_next 



simulate_step(1000, 0, 0.2, 10)




        