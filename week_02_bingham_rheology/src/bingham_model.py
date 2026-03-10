"""
Week 2: Bingham Plastic Rheology Model

Objective:
Model drilling fluid shear stress behavior using
the Bingham Plastic rheological model.

Author: Obua
"""

import numpy as np

#Create Bingham Model File

def bingham_shear_stress(yield_stress, plastic_viscosity, shear_rate):
    """
    Compute shear stress using the Bingham Plastic model.

    τ = τ0 + μp * γ

    Parameters
    ----------
    yield_stress : float
        Yield stress (Pa)

    plastic_viscosity : float
        Plastic viscosity (Pa·s)

    shear_rate : float or array
        Shear rate (1/s)

    Returns
    -------
    shear stress (Pa)
    """

    return yield_stress + plastic_viscosity * shear_rate

#Add Simple Test Case

if __name__ == "__main__":

    yield_stress = 5        # Pa
    plastic_viscosity = 0.02  # Pa·s

    shear_rates = np.linspace(0, 500, 50)

    stresses = bingham_shear_stress(
        yield_stress,
        plastic_viscosity,
        shear_rates
    )

    print("Example shear stress values:")
    print(stresses[:5])

