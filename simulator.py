"""
Physics simulator

Class for particle
    - attributes:
        - id
        - position (2/3 array)
        - velocity (2/3 array)
        - mass (float)
        - acceleration(2/3 array)

    - methods
        - calculate force
        - calculate acceleration
        - calculate new position

    - represented by circle/sphere
        -transform (2/3 array)
        * rotation (float)
        * colour

modules

    - gravity equation
    - acceleration calculator
    - velocity calculator

nuke
    - transform nodes for each particle
    - master circle
    - per frame animation

Scatter particles randomly
- Go through each in turn at each frame and work out force due to all other particles
- calculate acceleration vector
- work out new velocity
- work out new position

PLAY
"""

from objects import Particle
from random import random as rand
from config import LOG_FILE
import shelve


def random_in_range(range_list):
    """
    Gives random number in a certain range with step values

    Random.random gives number between 0 and 1
    Multiply by the range, then add the minimum
    :param range_list: [min, max, step]
    :return:
    """
    scale = range_list[1] - range_list[0]  # get total scale
    # print "Scale:", scale
    rand_seed = rand()  # get random number
    scaled_value = (rand_seed * scale) + range_list[0]

    return range_list[2] * round(scaled_value/range_list[2])


def generate_particles(num, mesh, v_range, m_range, planar=False):
    """
    Generate a bunch of particles distributed randomly
    Initial Velocities and their masses are also random

    :param num: How many particles
    :param mesh: Grid system to start the particles on
                list of lists for ranges, then a step size
                [[x_min, x_max], [y_min, y_max], [z_min, z_max], step]
    :param v_range: [v_min, v_max, v_step]
    :param m_range: [m_min, m_max, m_step]
    :return:
    """
    for i in range(3):
        print i
        mesh[i].append(mesh[3])
    # print mesh
    # print num
    for i in range(num):
        random_mass = random_in_range(m_range)
        random_position = [random_in_range(mesh[i]) for i in range(3)]
        random_velocity = [random_in_range(v_range) for i in range(3)]
        if not planar:
            random_velocity.append(random_in_range(v_range))
        Particle(random_mass, random_position, random_velocity)
        # print random_mass, random_position, random_velocity

    for particle in Particle.ALL_PARTICLES:
        print particle


def simulate_particles(num_steps):

    print "Starting Simulation:\nIteration: ",

    particle_dict = {}
    for particle in Particle.ALL_PARTICLES:
        particle_dict[particle.id] = {0: particle.x}

    for step in range(num_steps+1):
        print step,
        for particle in Particle.ALL_PARTICLES:
            particle.iterate()
            # print particle
            particle_dict[particle.id][particle.proper_time] = particle.x

    print "\nFinished Sim"
    for particle in Particle.ALL_PARTICLES:
        print particle
    return particle_dict

def export_dict(path_dict, sim_name):
    # print path_dict.keys()

    print "Writing Sim Data to File"
    d = shelve.open(LOG_FILE)
    d[sim_name] = path_dict
    d.close()

def main():

    # generate_particles(20, [[-1, 1], [-1, 1], [0, 0], 0.1], [-0.1, 0.1, 0.01], [1e5, 20e5, 1e4], planar=True)
    #generate_particles(100, [[0, 1920], [0, 1080], [0, 0], 1], [0, 0.01, 0.001], [1e5, 20e5, 1e4], planar=True)
    #generate_particles(30, [[0, 1920], [0, 1080], [0, 0], 1], [0, 0.1, 0.01], [1e10, 20e10, 1e4], planar=True)
    generate_particles(100, [[0, 700], [0, 500], [0, 0], 1], [0, 0.01, 0.001], [1e7, 20e7, 1e6], planar=True)
    path_dict = simulate_particles(100)
    export_dict(path_dict, '100_parts_e7')



if __name__ == "__main__":
    main()