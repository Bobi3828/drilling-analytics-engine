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




from temperature_model import correct_viscosity, temperature_profile

# Well parameters
surface_temp = 25
bottom_temp = 150
depth = 3000  # meters

depths, temps = temperature_profile(surface_temp, bottom_temp, depth)

well_results = []

for d, T in zip(depths, temps):

    visc = correct_viscosity(surface_viscosity, surface_temp, T, activation_energy)

    well_results.append({"depth_m": d, "temperature_C": T, "viscosity_cp": visc})

well_df = pd.DataFrame(well_results)

well_df.to_csv("../results/wellbore_viscosity_profile.csv", index=False)

print("Wellbore viscosity profile generated.")



from temperature_model import laminar_pressure_loss

# Flow parameters
flow_rate = 0.02
pipe_diameter = 0.1

pressure_losses = []

for i in range(len(well_df)):

    if i == 0:
        segment_length = 0
    else:
        segment_length = well_df["depth_m"][i] - well_df["depth_m"][i-1]

    viscosity = well_df["viscosity_cp"][i]

    pressure = laminar_pressure_loss(viscosity, flow_rate, segment_length, pipe_diameter)

    pressure_losses.append(pressure)

well_df["segment_pressure_loss_pa"] = pressure_losses
well_df["cumulative_pressure_loss_pa"] = well_df["segment_pressure_loss_pa"].cumsum()

well_df.to_csv("../results/wellbore_hydraulics_profile.csv", index=False)

print("Wellbore hydraulics simulation complete.")