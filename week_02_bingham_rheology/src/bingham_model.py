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

#Extend the Rheology Module

def calculate_bingham_parameters(theta600, theta300):
    """
    Calculate Bingham Plastic parameters from viscometer readings.

    Parameters
    ----------
    theta600 : float
        Viscometer dial reading at 600 RPM
    theta300 : float
        Viscometer dial reading at 300 RPM

    Returns
    -------
    PV : float
        Plastic viscosity (cP)

    YP : float
        Yield point (lb/100ft²)
    """

    PV = theta600 - theta300
    YP = theta300 - PV

    return PV, YP

#Add Example Test

if __name__ == "__main__":

    theta600 = 45
    theta300 = 30

    PV, YP = calculate_bingham_parameters(theta600, theta300)

    print("Plastic Viscosity:", PV)
    print("Yield Point:", YP)

#Convert Units for Shear Stress Model
       #     Your shear stress model expects Pascal units, not field units.



def convert_yp_to_pascal(yp):
    """
    Convert Yield Point from lb/100ft² to Pascal.
    converts the Yield Point (YP) from field units (lb/100ft²) to the SI unit of stress, Pascals (Pa)
    """
    return yp * 0.4788
