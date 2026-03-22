# Drillpipe Pressure Loss
import numpy as np

def drillpipe_pressure_loss(mu, velocity, diameter, length):
    """
    Simplified laminar flow pressure loss in drillpipe
    """

    dp = 32 * mu * velocity * length / (diameter ** 2)

    return dp

# Bit Nozzle Pressure Loss
def bit_pressure_loss(flow_rate, mud_density, nozzle_area):

    """
    Pressure drop across bit nozzles
    """

    velocity = flow_rate / nozzle_area

    dp = 0.5 * mud_density * velocity**2

    return dp

# Annular Pressure Loss
def annular_pressure_loss(dp_dz, depth):
    """
    Calculate total annular pressure loss.

    Parameters:
    dp_dz (float): Pressure gradient (Pa/m)
    depth (float): Well depth (m)

    Returns:
    float: Total annular pressure loss (Pa)
    """

    dp_total = dp_dz * depth

    return dp_total


# Total Standpipe Pressure
def standpipe_pressure(dp_pipe, dp_bit, dp_annulus):

    spp = dp_pipe + dp_bit + dp_annulus

    return spp