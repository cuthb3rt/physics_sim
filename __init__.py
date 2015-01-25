__author__ = 'Andy'
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