from vpython import *
import numpy as np


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


ball_radius = 0.4
num_of_pendulumns = 20
pend_step_size = 0.5
chord_var = 2.0
middle_chord = 10.0

pend_step = num_of_pendulumns * pend_step_size / (num_of_pendulumns - 1)
radius_step = chord_var / (num_of_pendulumns - 1)

colors = []
radii = []
chords = []
balls = []

length = num_of_pendulumns * pend_step_size + 1.0
mount = box(pos=vector(0, middle_chord + ball_radius / 2.0, length / 2.0),
            length=ball_radius, height=ball_radius,
            width=length)

color_vectors = get_color_vectors(num_of_pendulumns)

for i in range(num_of_pendulumns):
    radii.append(middle_chord - chord_var / 2.0 + i * radius_step)

    chords.append(cylinder(pos=vector(0, middle_chord,
                                      pend_step * i + pend_step_size),
                           axis=vector(0, -radii[-1], 0),
                           radius=0.025,
                           color=color.white))

    balls.append(sphere(radius=0.4,
                        pos=vector(0, middle_chord - radii[-1],
                                   pend_step * i + pend_step_size),
                        color=color_vectors[i]))

###############################################################################

count = 0.0
delta_t = 0.01

gravity = 9.81
disipate = 0.001

theta_steps = [pi / 3.0] * num_of_pendulumns
angles = [pi / 3.0] * num_of_pendulumns
theta_ds = [0.0] * num_of_pendulumns
theta_dds = [0.0] * num_of_pendulumns

while count < 1000000:
    rate(150)

    for i in range(num_of_pendulumns):
        chords[i].rotate(angle=theta_steps[i],
                         axis=vector(0, 0, 1))

        balls[i].rotate(angle=theta_steps[i],
                        axis=vector(0, 0, 1),
                        origin=vector(0, 10, pend_step * i))

        theta_dds[i] = - gravity / radii[i] * np.sin(angles[i]) \
                       - theta_ds[i] / radii[i] * disipate
        theta_ds[i] = theta_dds[i] * delta_t + theta_ds[i]
        theta_steps[i] = theta_ds[i] * delta_t
        angles[i] += theta_steps[i]

    if count == 0:
        sleep(2)

    count += 1

print('Done')
