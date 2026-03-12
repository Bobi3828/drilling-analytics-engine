Week 1: Temperature-Corrected Rheology Model

Problem

Drilling hydraulic calculations often rely on surface-measured rheological properties.

In high-temperature wells, viscosity degrades significantly with increasing temperature. Using uncorrected surface viscosity for downhole ECD and pressure loss calculations introduces modeling error.

This project builds a physics-based temperature correction engine using an Arrhenius-type viscosity relationship.


Engineering Objective


a) Quantify viscosity reduction with temperature

b) Model surface-to-downhole correction

c) Provide structured, reusable Python implementation

d) Lay foundation for improved ECD prediction systems


Model Basis


Arrhenius-type approximation:

μ(T) = μ₀ · exp[(Ea/R)(1/T − 1/T₀)]

Where:

μ₀ = surface viscosity

T₀ = surface temperature (Kelvin)

T = downhole temperature (Kelvin)

Ea = activation energy

R = universal gas constant


Assumptions


a) Single-phase fluid behavior

b) Constant activation energy

c) No shear-rate dependency in this phase

d) Laboratory calibration required for field accuracy


Limitations


a) Does not yet integrate Power Law K and n adjustments

b) Does not account for pressure effects

c) No field calibration included in Week 1


Next Steps


a) Sensitivity analysis

b) Visualization of viscosity vs temperature

c) Engineering interpretation of hydraulic impact


Initial Validation Results


The Arrhenius correction model shows exponential viscosity reduction with increasing temperature.

For a 35 cP surface viscosity at 25°C, downhole viscosity at 120°C reduces significantly depending on activation energy assumptions.

This confirms the necessity of temperature-adjusted rheological modeling in HPHT wells to avoid overestimation of hydraulic pressure losses.


Activation Energy Sensitivity


The model demonstrates strong dependence on activation energy (Ea).

Higher activation energy results in steeper viscosity degradation with temperature.

This highlights the need for laboratory calibration of Ea for specific drilling fluid systems.

Uncalibrated Ea values may introduce significant hydraulic modeling error in HPHT wells.


Hydraulic Impact Analysis


Temperature-corrected viscosity significantly reduces predicted pressure loss at elevated temperatures.

Using uncorrected surface viscosity overestimates hydraulic pressure losses, particularly in HPHT wells.

This demonstrates the importance of temperature-adjusted rheology in ECD and pump pressure prediction.


Hydraulic Model Limitation


The current pressure loss model assumes Newtonian laminar flow using the Hagen–Poiseuille relationship.

This simplification is used only to demonstrate the hydraulic impact of temperature-corrected viscosity.

Future development will replace this with Bingham Plastic and Herschel–Bulkley hydraulic correlations commonly used in drilling hydraulics modeling.


### Simulation Dataset

A temperature sweep simulation was performed from 25°C to 180°C to quantify viscosity degradation. Results are exported as a structured CSV dataset, enabling downstream analysis and visualization workflows.

# Why This Structure Matters

Right now your project has three layers:

a) Physics engine: src/temperature_model.py

b) Simulation runner: src/temperature_simulation.py

c) Analysis & visualization: notebooks/temperature_analysis.ipynb

### Wellbore Temperature Profile Simulation

A linear geothermal gradient was applied from surface to bottomhole conditions to simulate viscosity variation along the wellbore.
Results show progressive viscosity reduction with increasing depth, demonstrating the hydraulic implications of temperature-dependent rheology in deep wells.

### Wellbore Pressure Loss Simulation

Using the temperature-adjusted viscosity profile, pressure losses were calculated along the wellbore using a simplified laminar flow model.
Results demonstrate how temperature-induced viscosity reduction affects the cumulative hydraulic pressure profile.

This provides a foundation for future integration of Bingham Plastic and Herschel–Bulkley hydraulic correlations used in drilling engineering.