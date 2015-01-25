"""

"""

from objects import Particle
from random import random as rand
import file_io


def random_in_range(range_list):
    """
    Gives random number in a certain range with step values

    Random.random gives number between 0 and 1
    Multiply by the range, then add the minimum
    :param range_list: [min, max, step]
    :return:
    """
    scale = range_list[1] - range_list[0]  # get total scale
    if scale == 0:  # if no range is given, return the specified value
        return range_list[0]
    # print "Scale:", scale
    rand_seed = rand()  # get random number
    scaled_value = (rand_seed * scale) + range_list[0]

    return range_list[2] * round(scaled_value/range_list[2])


def generate_particles(num, mesh, v_range, m_range):
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
        # if not planar:
        #     random_velocity.append(random_in_range(v_range))
        Particle(random_mass, random_position, random_velocity)
        print random_mass, random_position, random_velocity

    for particle in Particle.ALL_PARTICLES:
        print particle


def simulate_particles(num_steps, delta_t, sim_name):

    print "Starting Simulation:\nIteration: ",

    particle_dict = {}
    for particle in Particle.ALL_PARTICLES:
        particle_dict[particle.id] = {0: particle.x}

    for step in range(num_steps+1):
        print step,
        for particle in Particle.ALL_PARTICLES:
            particle.iterate(delta_t)
            # print particle
            particle_dict[particle.id][particle.proper_time] = particle.x

    print "\nFinished Sim"
    for particle in Particle.ALL_PARTICLES:
        print particle

    file_io.export_dict(particle_dict, sim_name)


def main():

    #generate_particles(20, [[-1, 1], [-1, 1], [0, 0], 0.1], [-0.1, 0.1, 0.01], [1e5, 20e5, 1e4], planar=True)
    #generate_particles(100, [[0, 1920], [0, 1080], [0, 0], 1], [0, 0.01, 0.001], [1e5, 20e5, 1e4], planar=True)
    #generate_particles(30, [[0, 1920], [0, 1080], [0, 0], 1], [0, 0.1, 0.01], [1e10, 20e10, 1e4], planar=True)
    # generate_particles(100, [[0, 700], [0, 500], [0, 0], 1], [0, 0.0, 0.001], [1e7, 20e7, 1e6], planar=True)
    generate_particles(100, [[0, 700], [0, 500], [0, 0], 1], [0, 0, 0], [1e7, 20e7, 1e6], planar=True)
    simulate_particles(100, 'train_sim')

if __name__ == "__main__":
    main()