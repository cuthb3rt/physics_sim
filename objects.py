__author__ = 'Andy'

import physics
import vec_math as vm


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
        return "%s\tm: %s\tx: %s\tv: %s\ta: %s" % (self.id, self.m, vm.v_pretty(self.x), vm.v_pretty(self.v), vm.v_pretty(self.a))

    def __init__(self, m, i_x, i_v):
        self.id = Particle.NUM_PARTICLES
        Particle.NUM_PARTICLES += 1
        Particle.ALL_PARTICLES.append(self)

        self.m = m
        self.x = [float(i) for i in i_x]
        self.v = [float(i) for i in i_v]
        self.a = vm.NULL_VEC
        self.proper_time = 0

    def update_acceleration(self):
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

        self.a = vm.v_div(res_f, self.m)

    def update_velocity(self, delta_t):
        """
        Assume that velocity is initial plus acceleration*time interval
        :return:
        """
        self.v = vm.v_add(self.v, vm.v_mult(self.a, delta_t))

    def update_position(self, delta_t):
        """
        Assume that new position is old position plus velocity*time interval
        :return:
        """
        self.x = vm.v_add(self.x, vm.v_mult(self.v, delta_t))

    def iterate(self, delta_t):
        self.update_acceleration()
        self.update_velocity(delta_t)
        self.update_position(delta_t)
        self.proper_time += delta_t
