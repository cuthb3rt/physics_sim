__author__ = 'Andy'

import nuke
from objects import Particle
from simulator import generate_particles, simulate_particles


def nuke_test():

    # Create basic colorwheel
    cw = nuke.createNode("ColorWheel")
    print cw

    generate_particles(10, [[-1, 1], [-1, 1], [0, 0], 0.1], [-0.1, 0.1, 0.01], [1e5, 20e5, 1e4], planar=True)

    # Create a transform node for each particle
    for particle in Particle.ALL_PARTICLES:
        particle.tf = nuke.createNode("Transform")


    path_dict = simulate_particles(100)

	
### To be run inside nuke
import nuke
import physics_sim.simulator as ps
from physics_sim.objects import Particle
	
cw = nuke.Node("ColorWheel")
cwt = nuke.Node("Transform")
cwt.knob("scale").setValue(0.05)

ps.generate_particles(50, [[-800, 800], [-500, 500], [0, 0], 10], [-5, 5, 1], [1e5, 20e5, 1e4], planar=True)

transforms = []
for particle in Particle.ALL_PARTICLES:

    particle.tf = nuke.Node("Transform")
    particle.tf.setInput(0, cwt)
    particle.tf.setName("Particle_%s_Transform" % particle.id)
    transforms.append(particle.tf)
    particle.tf.knob('translate').setAnimated()
	particle.tf.knob('translate').setValueAt(particle.x[0], 0, 0)
	particle.tf.knob('translate').setValueAt(particle.x[1], 0, 1)

for i in transforms:
    i.setSelected(True)
	
print "Create A Merge Node with these selected..."

path_dict = ps.simulate_particles(300)

for particle in Particle.ALL_PARTICLES:
    frame_dict = path_dict[particle.id]
    for time, position in frame_dict.iteritems():
		particle.tf.knob('translate').setValueAt(position[0], time, 0)
		particle.tf.knob('translate').setValueAt(position[1], time, 1)