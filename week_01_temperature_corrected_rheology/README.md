# Temperature-Corrected Drilling Fluid Rheology Model

## Overview

Hydraulic calculations in drilling operations are typically based on surface-measured drilling fluid rheology. In high-temperature wells, however, viscosity degrades significantly with temperature. Using uncorrected surface viscosity in hydraulic models introduces substantial error in:

a) Equivalent Circulating Density (ECD)

b) Pump pressure prediction

c) Annular pressure loss estimation

This project develops a physics-based temperature correction model for drilling fluid viscosity using an Arrhenius-type relationship. The goal is to demonstrate how data science and physical modeling can improve hydraulic predictions in drilling engineering, particularly in high-pressure high-temperature (HPHT) wells.

This project is part of a broader portfolio exploring data-driven solutions for drilling fluid and wellbore hydraulics problems in the oil and gas industry.


# Engineering Objective

The project aims to:

a) Quantify viscosity degradation with temperature.

b) Build a surface-to-downhole viscosity correction model.

c) Implement the model in structured, reusable Python code.

d) Demonstrate the hydraulic impact of temperature-dependent rheology.

Ultimately, the work forms a building block toward data-driven ECD prediction systems for drilling operations.


# Physical Model

Drilling fluid viscosity is modeled using an Arrhenius-type temperature relationship:

corrected_viscosity, μ(T) = surface_viscosity, μ₀ * np.exp((activation_energy,Ea / R) * (1 / T_downhole_k, T - 1 / T_surface_k, T₀ )

Where:

                                     μ(T) — viscosity at downhole temperature

                                     μ₀ — surface viscosity

                                     T₀ — surface temperature (Kelvin)

                                     T — downhole temperature (Kelvin)

                                     Eₐ — activation energy

                                     R — universal gas constant

This relationship approximates the thermal degradation behavior of drilling fluid viscosity.


# Project Architecture

The project follows a modular structure common in production data science systems.

project/
│
├── src/
│   ├── temperature_model.py
│   │   Physics-based viscosity correction engine
│   │
│   └── temperature_simulation.py
│       Simulation framework for temperature sweep experiments
│
├── notebooks/
│   └── temperature_analysis.ipynb
│       Data analysis and visualization
│
└── data/
    Simulation outputs (CSV datasets)

The project separates:

a) Physics modeling

b) Simulation execution

c) Data analysis & visualization

This structure supports scalability for more advanced drilling hydraulics modeling.


# Simulation Experiments

## Temperature Sweep Study

A temperature sweep simulation from 25°C to 180°C was performed to quantify viscosity degradation.

The results confirm the expected exponential decrease in viscosity with increasing temperature, consistent with Arrhenius-type behavior.

Simulation outputs are exported as structured CSV datasets to enable reproducible analysis and visualization workflows.


## Activation Energy Sensitivity Analysis

The model shows strong sensitivity to activation energy (Ea).

Higher activation energy values produce steeper viscosity reduction curves, highlighting the importance of laboratory calibration for specific drilling fluid systems.

Without proper calibration, hydraulic predictions in HPHT wells can contain significant error.


## Wellbore Temperature Profile Simulation

To simulate downhole conditions, a linear geothermal gradient was applied from surface to bottomhole depth.

This allows estimation of viscosity variation along the wellbore, demonstrating how drilling fluid rheology evolves during circulation.

The results show a progressive viscosity reduction with depth, reinforcing the need for temperature-corrected rheology models in deep wells.

## Hydraulic Impact Demonstration

Using the temperature-corrected viscosity profile, pressure losses along the wellbore were calculated.

For demonstration purposes, the model uses a simplified laminar flow relationship derived from the Hagen–Poiseuille equation.

The results show that:

a) Surface viscosity overestimates pressure losses

b) Temperature-corrected viscosity produces lower hydraulic pressure predictions

This highlights the importance of incorporating temperature effects into ECD and pump pressure calculations.


# Model Assumptions

a) Single-phase drilling fluid

b) Constant activation energy

c) No shear-rate dependency

d) Temperature as the primary viscosity driver

These assumptions simplify the model for the initial development stage.
 

## Current Limitations

This first version does not yet include:

a) Power Law K and n rheology adjustments

b) Pressure effects on viscosity

c) Field or laboratory calibration datasets

d) Non-Newtonian drilling fluid behavior


## Future Development

Planned extensions include:

a) Bingham Plastic and Herschel–Bulkley hydraulic models

b) Integration of Power Law rheology parameters

c) Pressure-temperature coupled viscosity models

d) Field data calibration

e) Machine learning models for ECD prediction and hydraulic optimization


### Why This Project Matters

Drilling hydraulic modeling remains heavily dependent on simplified assumptions and surface measurements.

By combining physical models with data science workflows, this project demonstrates how modern analytics can improve:

a) Drilling hydraulics prediction

b) ECD management

c) Wellbore stability analysis

d) Drilling efficiency in HPHT environments



**Author**

Obua Innocent

Drilling & Completion Fluids Engineer
Data Science Practitioner

Experience in drilling fluid engineering, wellsite operations, and data-driven engineering modeling for the oil and gas industry.

This repository is part of a larger portfolio focused on applying data science to drilling engineering challenges.