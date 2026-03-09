import numpy as np
import pandas as pd
from temperature_model import correct_viscosity

# Base parameters
surface_viscosity = 35
T_surface = 25
activation_energy = 25000

# Temperature range
temperatures = np.linspace(25, 180, 60)

results = []

for T in temperatures:
    corrected = correct_viscosity(surface_viscosity, T_surface, T, activation_energy)

    results.append({"temperature_C": T, "corrected_viscosity_cp": corrected})

df = pd.DataFrame(results)

# Save results
df.to_csv("../results/temperature_viscosity_table.csv", index=False)

print("Simulation complete. Results saved.")