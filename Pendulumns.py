from vpython import *
import numpy as np
import sys
import time


# Function to create a rainbow of colors for the pendulum balls
def get_color_vectors(num_of_pendulumns):
    color_step_size = 2.0 / num_of_pendulumns

    def val_adjust(val):
        if val < 0.0:
            val = 0.0
        elif val > 1.0:
            val = 0.0

        return val

    color_vectors = []
    rnd_amt = 3

    for i in range(num_of_pendulumns):
        vals = 1.0 - color_step_size * i

        val1 = val_adjust(round(+vals, rnd_amt))

        val2a = val_adjust(round(1.0 + vals, rnd_amt))
        val2b = val_adjust(round(1.0 - vals, rnd_amt))
        val2 = val2a + val2b
        val2 = 1.0 if val2 > 1.0 else val2

        val3 = val_adjust(round(-vals, rnd_amt))

        color_vectors.append(vector(val1, val2, val3))

    return color_vectors


# Parameters for the visual python objects
ball_radius = 0.4
num_of_pendulumns = 20
pend_step_size = 0.5
chord_var = 2.0  # overall chord variation - shortest to longest
middle_chord = 10.0

# Parameters to control the gradual changes in pendulums
pend_step = num_of_pendulumns * pend_step_size / (num_of_pendulumns - 1)
radius_step = chord_var / (num_of_pendulumns - 1)

# Initiation of storage arrays to hold information for the pendulums
colors = []
radii = []
chords = []
balls = []

# Length parameter for the mount that the pendulums will connect to and a
#     call to the VP box class to instantiate the mount object
length = num_of_pendulumns * pend_step_size + 1.0
mount_ht = middle_chord / 2.0 + ball_radius / 2.0
mount = box(pos=vector(0, mount_ht, length / 2.0),
            axis=vector(0, 0, length),
            width=ball_radius,
            height=ball_radius)

# The call to the get_color_vectors function
color_vectors = get_color_vectors(num_of_pendulumns)

# For each pendulum, calc the radius, and draw its chord and ball
for i in range(num_of_pendulumns):
    radii.append(middle_chord - chord_var / 2.0 + i * radius_step)

    chords.append(cylinder(pos=vector(0, middle_chord / 2.0,
                                      pend_step * i + pend_step_size),
                           axis=vector(0, -radii[-1], 0),
                           radius=0.025,
                           color=color.white))

    balls.append(sphere(radius=0.4,
                        pos=vector(
                            0,
                            middle_chord / 2.0 - radii[-1],
                            pend_step * i + pend_step_size),
                        color=color_vectors[i]))

time.sleep(4)
###############################################################################
# Dynamic Section
# Parameters for the physics
gravity = 9.81
f_d = 0.01

# Parameters for the numerical simulation
count = 0.0
delta_t = 0.01

# Initialization of the state variables
theta = [np.pi / 3.0] * num_of_pendulumns
theta_steps = [np.pi / 3.0] * num_of_pendulumns
theta_d = [0.0] * num_of_pendulumns
theta_dd = [0.0] * num_of_pendulumns

# A while loop to control the time steps of the numerical simulation
while count < 1000000:
    rate(150)

    # Update rotation about the mounts for each pendulum
    for i in range(num_of_pendulumns):
        chords[i].rotate(angle=theta_steps[i],
                         axis=vector(0, 0, 1))

        balls[i].rotate(angle=theta_steps[i],
                        axis=vector(0, 0, 1),
                        origin=vector(
                            0,
                            + middle_chord / 2.0,
                            pend_step * i + pend_step_size))

        # Update the state variables using numerical integration
        theta_dd[i] = - gravity / radii[i] * np.sin(theta[i]) \
            - f_d * theta_d[i] ** 2
        theta_d[i] += theta_dd[i] * delta_t
        theta_steps[i] = theta_d[i] * delta_t  # for VP object movements
        theta[i] += theta_steps[i]

    if count == 0:
        sleep(4)

    count += 1
