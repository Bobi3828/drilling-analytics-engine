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
    Calculate shear stress using Herschel-Bulkley model
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