"""
Module providing basic vector math
"""
__author__ = 'Andy'

import math
from config import N_DIMS

NULL_VEC = [0.0 for i in range(N_DIMS)]

def v_pretty(v):
    return ["%02f" % i for i in v]


def v_mag(v):
    return math.sqrt(sum([(v[i]**2) for i in range(N_DIMS)]))


def v_norm(v):
    return v_div(v, v_mag(v))


def v_mult(v, n):
    return [v[i] * n for i in range(N_DIMS)]


def v_div(v, n):
    return v_mult(v, 1.0/n)


def v_sub(v1, v2):
    return [(v1[i] - v2[i]) for i in range(N_DIMS)]


def v_add(v1, v2):

    return [v1[i] + v2[i] for i in range(N_DIMS)]

