"""
Week 3: Herschel–Bulkley Rheology Model

Objective:
Model non-Newtonian drilling fluid behaviour
using the Herschel–Bulkley equation.

Author: Obua
"""

import numpy as np

# Create Model File


def herschel_bulkley_shear_stress(yield_stress, K, n, shear_rate):

    """
    Calculate shear stress using Herschel–Bulkley model
    """

    shear_stress = yield_stress + K * (shear_rate ** n)

    return shear_stress

# Test the model

if __name__ == "__main__":

    yield_stress = 6   # Pa
    K = 0.4            # consistency index
    n = 0.65           # flow behaviour index

    shear_rates = np.linspace(0, 500, 50)

    stresses = herschel_bulkley_shear_stress(
        yield_stress,
        K,
        n,
        shear_rates
    )

    print(stresses[:5])


# Upgrade the Model File

import numpy as np

R = 8.314  # universal gas constant


def temperature_adjusted_K(K0, Ea, T_surface, T_downhole):

    """
    Arrhenius temperature correction for Herschel-Bulkley consistency index
    """

    T_surface_K = T_surface + 273.15
    T_downhole_K = T_downhole + 273.15

    K_T = K0 * np.exp(Ea/R * (1/T_downhole_K - 1/T_surface_K)) # the shear thinning of drilling fluids, the negative sign(-) in the Ea is removed 
                                                                #otherwise the value of k will increase, not depicting actual drilling situation

    return K_T