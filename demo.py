__author__ = 'Andy'

import simulator
import nuke_render

if __name__ == "__main__":

    mesh = [[710, 1260], [270, 810], [0, 0], 10]  # confine to an area within the frame
    velocity_range = [0, 0, 0]  # start with stationary particles
    mass_range = [1e13, 1e13, 1]  # fairly massive particles

    sim_name = 'sim_name'
    num_particles = 2
    sim_iterations = 10
    delta_t = 1

    print "Generating particles..."
    simulator.generate_particles(num_particles, mesh, velocity_range, mass_range)
    simulator.simulate_particles(sim_iterations, delta_t, sim_name)
    nuke_render.render(sim_name)