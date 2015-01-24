__author__ = 'Andy'

import physics
import vec_math as vm
from config import DELTA_T


class Particle():
    """
    Particle class
    mass = float
    i_p = 3vec
    i_v = 3vec
    """
    NUM_PARTICLES = 1
    ALL_PARTICLES = []

    def __repr__(self):
        # return "ID: %s; Mass: %s; Position: %s; Velocity: %s; Acceleration: %s" % (self.id, self.m, self.x, self.v, self.a)
        return "%s\t%s\t%s\t%s\t%s" % (self.id, self.m, vm.v_pretty(self.x), vm.v_pretty(self.v), vm.v_pretty(self.a))

    def __init__(self, m, i_x, i_v):
        self.id = Particle.NUM_PARTICLES
        Particle.NUM_PARTICLES += 1
        Particle.ALL_PARTICLES.append(self)

        self.m = m
        self.x = [float(i) for i in i_x]
        self.v = [float(i) for i in i_v]
        self.a = vm.NULL_VEC
        self.proper_time = 0

    @property
    def new_acceleration(self):
        """
        Calculate acceleration due to all other particles

        TODO
                force_dict = {self.id: [0, 0, 0]}
                set up a dictionary of the force due to each particle
                then can have already calculated the force due to most particles by the end time...
                will almost halve sim times
        :return:
        """
        res_f = [0, 0, 0]  # resultant force so far
        for particle in Particle.ALL_PARTICLES:
            if not particle.id == self.id:  # don't count force due to itself...
                force = physics.calculate_force(self, particle)
                res_f = vm.v_add(res_f, force)
                # print "Force on %s due to %s = %s" % (self.id, particle.id, res_f)

        # print res_f

        return vm.v_div(res_f, self.m)

    @property
    def new_velocity(self):
        """
        Assume that velocity is initial plus acceleration*time interval
        :return:
        """
        return vm.v_add(self.v, vm.v_mult(self.a, DELTA_T))

    @property
    def new_position(self):
        """
        Assume that new position is old position plus velocity*time interval
        :return:
        """
        return vm.v_add(self.x, vm.v_mult(self.v, DELTA_T))

    def iterate(self):
        self.a = self.new_acceleration
        self.v = self.new_velocity
        self.x = self.new_position
        self.proper_time += DELTA_T
