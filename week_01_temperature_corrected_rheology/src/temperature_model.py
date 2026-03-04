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


if __name__ == "__main__":
    # Test case parameters
    surface_viscosity = 35      # cP
    T_surface = 25              # °C
    T_downhole = 120            # °C
    activation_energy = 25000   # J/mol (example value)

    corrected = correct_viscosity(
        surface_viscosity,
        T_surface,
        T_downhole,
        activation_energy
    )

    print(f"Surface viscosity: {surface_viscosity} cP")
    print(f"Corrected viscosity at {T_downhole}°C: {corrected:.2f} cP")

    # Sanity check
    assert corrected < surface_viscosity, \
        "Viscosity should decrease with increasing temperature"