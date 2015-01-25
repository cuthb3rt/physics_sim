__author__ = 'Andy'

import simulator
import nuke_render

if __name__ == "__main__":

    # :param mesh: Grid system to start the particles on
    #             list of lists for ranges, then a step size
    #             [[x_min, x_max], [y_min, y_max], [z_min, z_max], step]
    # :param v_range: [v_min, v_max, v_step]
    # :param m_range: [m_min, m_max, m_step]

    mesh = [[350, 1050], [250, 750], [0, 0], 1]  # confine to an area within the frame
    velocity_range = [0, 0, 0]  # start with stationary particles
    mass_range = [1e20, 6e20, 1e20]  # fairly massive particles

    sim_name = 'train_sim'
    num_particles = 10
    sim_iterations = 100
    delta_t = 1

    print "Generating particles..."
    simulator.generate_particles(num_particles, mesh, velocity_range, mass_range)
    simulator.simulate_particles(sim_iterations, sim_name, delta_t)
    nuke_render.render(sim_name)