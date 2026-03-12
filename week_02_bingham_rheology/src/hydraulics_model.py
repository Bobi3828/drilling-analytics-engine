# Add Hydraulics Function

"""
Week 2: Annular Hydraulics Model

Objective:
Estimate laminar pressure loss in the annulus using
Bingham Plastic rheology.

Author: Obua
"""

import numpy as np


def annular_pressure_loss(mu_p, yield_stress, flow_rate, dh, dp):

    """
    Estimate laminar pressure loss in annulus.

    Parameters
    ----------
    mu_p : float
        Plastic viscosity (Pa.s)

    yield_stress : float
        Yield stress (Pa)

    flow_rate : float
        Flow rate (m3/s)

    dh : float
        Hole diameter (m)

    dp : float
        Pipe diameter (m)

    Returns
    -------
    pressure_gradient : float
        Pressure loss per meter (Pa/m)

        
  # Total Pressure Gradient
    pressure_gradient = viscous_term + yield_term
            Yield Component (Stress to overcome Yield Point)
            Viscous Component (Friction from Plastic Viscosity) 
    """

    annular_area = (np.pi / 4) * (dh**2 - dp**2)

    velocity = flow_rate / annular_area

    hydraulic_diameter = dh - dp # Equivalent (Hydraulic) Diameter

    pressure_gradient = ((32 * mu_p * velocity) / (hydraulic_diameter**2) + (4 * yield_stress / hydraulic_diameter))

    return pressure_gradient