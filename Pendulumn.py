import numpy as np
from Plot_Tools import Basic_Plot as BP

radius = 0.1
gravity = 9.81
f_d = 0.1

theta = np.pi / 3.0
theta_list = [theta]
theta_d = 0.0

time = 0.0
delta_t = 0.01
time_list = [0.0]
count = 0.0

while count < 10000:
    theta_dd = gravity / radius * np.sin(theta) \
        - f_d * theta_d ** 2.0
    theta_d += theta_dd * delta_t
    theta += theta_d * delta_t

    theta_list.append(theta)
    time += delta_t
    time_list.append(time)

    count += 1

BP(x=time_list, y=theta_list,
   t='Theta vs. Time',
   x_t='Time Values', y_t='Theta Values')
