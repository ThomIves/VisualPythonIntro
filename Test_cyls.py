from vpython import *

cylinder(pos=vector(0, 0, 0),
         axis=vector(10, 0, 0),
         radius=0.025,
         color=color.red)

cylinder(pos=vector(0, 0, 0),
         axis=vector(0, 10, 0),
         radius=0.025,
         color=color.blue)

cylinder(pos=vector(0, 0, 0),
         axis=vector(0, 0, 10),
         radius=0.025,
         color=color.green)
