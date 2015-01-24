__author__ = 'Andy'

import nuke
import os
import shelve

def read_db(sim_name):

    d = shelve.open("C:/Users/Andy/.nuke/sys.PYTHON/physics_sim/log/sim_log.txt")
    print d.keys()
    sim_dict = d[sim_name]
    d.close()

    return sim_dict

def render(sim_name, version=1):

    sim_dict = read_db(sim_name)

    output_dir = 'C:/Nuke/renders/%s_v%03d' % (sim_name, version)
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)
    output_seq = '%s/%s_v%03d.%%04d.jpg' % (output_dir, sim_name, version)
    output_script = '%s/%s_v%03d.nk' % (output_dir, sim_name, version)

    sim_dict = read_db(sim_name)
    # print sim_dict

    nuke.root()["format"].setValue("HD_1080")
    # Create Colour_Wheel and tranform it
    cw = nuke.nodes.ColorWheel()
    cwt = nuke.nodes.Transform(scale=0.05)
    cwt.setInput(0, cw)
    # print cwt

    frame_range = [0, 0]
    transforms = []
    previous_merge = None
    for particle_id in sim_dict.keys():
        # print "Processing Particle %s" % particle_id,
        tf = nuke.nodes.Transform(name="Particle_%s_transform" % particle_id)
        tf.setInput(0, cwt)
        transforms.append(tf)
        tf.knob('translate').setAnimated()
        # Run through each of the frame values
        path_dict = sim_dict[particle_id]
        frame_range = [min(path_dict.keys()), max(path_dict.keys())]
        for frame in path_dict.keys():
            print frame, path_dict[frame],
            tf.knob('translate').setValueAt(path_dict[frame][0], frame, 0)  # set x position
            tf.knob('translate').setValueAt(path_dict[frame][1], frame, 1)  # set y position

        new_merge = nuke.nodes.Merge()
        new_merge.setInput(0, tf)
        if previous_merge:
            new_merge.setInput(1, previous_merge)
        previous_merge = new_merge

        # print "."

    print frame_range

    # set the frame range to match
    nuke.root()["first_frame"].setValue(frame_range[0])
    nuke.root()["last_frame"].setValue(frame_range[1])

    write = nuke.nodes.Write()
    write.setInput(0, previous_merge)

    write['file'].setValue(output_seq)
    write['file_type'].setValue('jpg')
    write['_jpeg_quality'].setValue(0.75)
    nuke.execute(write, frame_range[0], frame_range[1], 1)
    nuke.scriptSave(output_script)

# run with sim name and maybe version
render('100_parts_e7')