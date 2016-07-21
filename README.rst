This is the documentation for https://github.com/cuthb3rt/physics_sim

The docs are available on GitHub Pages here: http://cuthb3rt.github.io/physics_sim

Basic Particle Simulator Using nuke to render images of the particles

Just a little project to try out simulating forces and particles using vectors etc.
Also using Nuke (currently) to visualize the particles.
Current implementation uses colour wheels distributed around the image with keyframes at the simulated time steps.

Currently runs in 2 parts:

    1. Simulation
        -   Create the particles and set up the initial configuration/distribution
        -   Run the simulation
        -   Output the results to a text file (currently stored using shelve as a dictionary)
    2. Visualisation
        -   Nuke 9 python module implemented
        -   Create a colour wheel and scale it down, then apply an animated
            transform for every particle and merge them together
        -   Render out an Image Sequence with the results and save the script to that folder

Issues/Possible Features:

- Particles don't collide, they just swoosh around each other.
- Add some boundary forces to see if they're touching
    - Can then set the bounce forces (ie how much does the velocity scale when they hit...)
    - Can also take into account the fact that within the particle, the force decreases linearly (this will counteract
        the infinite force when they're in the same place...)
- Maybe add the ability to manually place particles and sim from there / override the velocities...
- Would be nice to increase the granularity of the simulation for shorter time intervals (more precision)
  while keeping the same playback info
- Maybe apply burnins to the output containing sim data