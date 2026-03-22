import numpy as np

def annular_shear_rate(flow_rate, hole_diameter, pipe_diameter):
    annular_area = np.pi * (hole_diameter**2 - pipe_diameter**2) / 4
    velocity = flow_rate / annular_area
    hydraulic_diameter = hole_diameter - pipe_diameter

    shear_rate = 8 * velocity / hydraulic_diameter

    return shear_rate


def pressure_gradient_hb(mu_app, velocity, hydraulic_diameter):
    dp_dz = 32 * mu_app * velocity / (hydraulic_diameter**2)
    return dp_dz

