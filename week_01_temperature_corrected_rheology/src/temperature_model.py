"""
Week 1: Temperature-Corrected Rheology Engine

Objective:
Model the effect of temperature on drilling fluid viscosity
using an Arrhenius-based correction model.

Author: Obua
"""

import numpy as np

# Universal gas constant (J/mol·K)
R = 8.314


def celsius_to_kelvin(temp_c):
    """
    Convert temperature from Celsius to Kelvin.
    """
    return temp_c + 273.15


def correct_viscosity(surface_viscosity, T_surface_c, T_downhole_c, activation_energy):
    """
    Apply Arrhenius temperature correction to viscosity.

    Parameters:
    surface_viscosity (float): viscosity at surface temperature
    T_surface_c (float): surface temperature in Celsius
    T_downhole_c (float): downhole temperature in Celsius
    activation_energy (float): activation energy (J/mol)

    Returns:
    float: corrected viscosity at downhole temperature
    """
    
    T_surface_k = celsius_to_kelvin(T_surface_c)
    T_downhole_k = celsius_to_kelvin(T_downhole_c)
    
    if T_downhole_c < -273.15 or T_surface_c < -273.15:
        raise ValueError("Temperature below absolute zero is invalid.")
    
    if surface_viscosity <= 0:
        raise ValueError("Surface viscosity must be positive.")

    corrected_viscosity = surface_viscosity * np.exp(
        (activation_energy / R) * (1 / T_downhole_k - 1 / T_surface_k)
    )

    return corrected_viscosity

def laminar_pressure_loss(viscosity_cp, flow_rate_m3s, pipe_length_m, pipe_diameter_m):
    viscosity_pa_s = viscosity_cp / 1000  # convert cP to Pa·s

    pressure_loss = ((128 * viscosity_pa_s * pipe_length_m * flow_rate_m3s) /(np.pi * pipe_diameter_m**4))
    return pressure_loss


if __name__ == "__main__":
    # Test case parameters
    surface_viscosity = 35      # cP
    T_surface = 25              # °C
    T_downhole = 120            # °C
    activation_energy = 25000   # J/mol (example value)

    corrected = correct_viscosity(surface_viscosity, T_surface, T_downhole, activation_energy)

    print(f"Surface viscosity: {surface_viscosity} cP")
    print(f"Corrected viscosity at {T_downhole}°C: {corrected:.2f} cP")

    # Sanity check
    assert corrected < surface_viscosity, \
        "Viscosity should decrease with increasing temperature"
    

    
    #This is simplified laminar flow physics. We’re not modeling turbulence yet.
    # Estimate laminar pressure loss using simplified Hagen–Poiseuille relationship.

    #Parameters:
    # viscosity_cp (float): viscosity in cP, flow_rate_m3s (float): volumetric flow rate (m³/s), pipe_length_m (float): pipe length (m), pipe_diameter_m (float): pipe diameter (m)
    # Returns:
    # float: pressure loss (Pa)

    
    

    # Hydraulic impact example

    flow_rate = 0.02        # m3/s (example)
    pipe_length = 1000      # m
    pipe_diameter = 0.1     # m

    surface_pressure = laminar_pressure_loss(surface_viscosity, flow_rate, pipe_length, pipe_diameter)

    downhole_pressure = laminar_pressure_loss(corrected, flow_rate, pipe_length, pipe_diameter)

    print(f"Surface pressure loss: {surface_pressure:.2f} Pa")
    print(f"Downhole pressure loss: {downhole_pressure:.2f} Pa")


def temperature_profile(surface_temp_c, bottom_temp_c, depth_m, steps=50):
    """
    Generate a linear temperature profile along the well depth.

    Parameters
    ----------
    surface_temp_c : float
        Surface temperature (°C)
    bottom_temp_c : float
        Bottomhole temperature (°C)
    depth_m : float
        Total well depth
    steps : int
        Number of depth points

    Returns
    -------
    depths : array
    temperatures : array
    """

    depths = np.linspace(0, depth_m, steps)
    temperatures = np.linspace(surface_temp_c, bottom_temp_c, steps)

    return depths, temperatures