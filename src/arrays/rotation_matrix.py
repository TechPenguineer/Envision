from math import *
import numpy as np
from view import *
rotation_z = np.matrix([
    [cos(angle), -sin(angle), 0],
    [sin(angle), cos(angle), 0],
    [0,0,1]
])
angle += 0.01