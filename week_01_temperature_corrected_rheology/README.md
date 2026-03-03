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