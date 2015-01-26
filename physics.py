"""
Module providing physics calculations
"""

__author__ = 'Andy'

import vec_math

G = 6.673e-11
# g = 9.81


def calculate_force(p1, p2):
    """
    Calculates the force on particle1 due to particle2 (and vice versa)
    """
    direction = vec_math.v_sub(p1.x, p2.x)  # direction vector of the force
    sep = vec_math.v_mag(direction)  # separation of the 2 particles
    if sep <= 100.0:  # Make the approximation that within 1 meter, there is no force
        return vec_math.NULL_VEC
    # try:
    f_m = - (G * p1.m * p2.m) / sep ** 2  # magnitude of the force
    # except ZeroDivisionError:
    #     return vec_math.NULL_VEC

    f_v = [f_m * i for i in vec_math.v_norm(direction)]  # force vector is normalised vector * force magnitude
    # print "Force: %s" % f_v
    return f_v