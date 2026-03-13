# Bingham Plastic Drilling Fluid Rheology Model

## Overview

Drilling fluids are non-Newtonian, exhibiting yield stress and shear-dependent viscosity. Simple Newtonian models fail to capture this behavior, leading to inaccurate hydraulic predictions.

This project implements a Bingham Plastic rheology model to represent drilling fluids more realistically, integrating field viscometer data, temperature correction, and downhole hydraulic modeling. The result is a computational drilling hydraulics engine capable of estimating pressure losses and ECD along the wellbore.

# Engineering Objective

a) Convert viscometer readings (θ600, θ300) into Bingham Plastic parameters: Plastic Viscosity (PV), and Yield Point (YP).

b) Apply temperature correction to reflect downhole conditions.

c) Generate shear stress vs shear rate curves for multiple muds.

d) Compute annular pressure loss and Equivalent Circulating Density (ECD).

e) Build a reproducible, Python-based workflow for drilling hydraulics analysis.

This workflow bridges mud lab measurements, rheology modeling, and drilling engineering simulations.



# Bingham Plastic Model

The Bingham Plastic model expresses shear stress as:
τ = τ0 + μp γ

Where:
                                         τ = shear stress
                                         τ0 = yield stress
                                         μp = plastic viscosity
                                         γ = shear rate

This model is widely used in drilling hydraulics for pressure loss calculations and mud selection.

## Field Data Integration

Field viscometer measurements are converted to engineering units:


                             PV = θ600 − θ300, field units (centipoise, cP), divide by 1000 to convert to Pa.s
                             YP = θ300 − PV, field units (lb/100ft²), multiply by 0.4788 to convert it to Pa

This standardization enables downhole pressure calculations in SI units and aligns the simulation with real mud lab workflows.


# Computational Workflow

The full workflow now models a complete drilling hydraulics chain:

                                         Viscometer data (θ600, θ300)
                                                   ↓
                                           PV / YP calculation
                                                   ↓
                                       Bingham Plastic rheology curve
                                                   ↓
                                    Temperature correction (Arrhenius model)
                                                   ↓
                                          Downhole rheology profile
                                                   ↓
                                      Annular pressure loss calculation
                                                   ↓
                                      Equivalent Circulating Density (ECD)


Each step is modular, allowing easy extension to multiple muds, deeper wells, and more complex rheology models.



# Temperature-Corrected Rheology

Surface viscometer readings are adjusted for downhole temperature using the Arrhenius viscosity correction:

corrected_viscosity, μ(T) = surface_viscosity, μ₀ * np.exp(
        (activation_energy,Ea / R) * (1 / T_downhole_k, T - 1 / T_surface_k, T₀ )


Where:

                                 μ(T) — viscosity at downhole temperature

                                 μ₀ — surface viscosity

                                 T₀ — surface temperature (Kelvin)

                                 T — downhole temperature (Kelvin)

                                 Eₐ — activation energy

                                 R — universal gas constant

This ensures that high-temperature wells are modeled realistically, avoiding overestimation of hydraulic pressures and ECD.


# Annular Pressure Loss and ECD

Pressure loss along the annulus is converted to ECD using:

ECD = MW + (ΔP / (0.052 × TVD))

Where:

                                 MW  = mud weight (ppg)
                                 ΔP  = annular pressure loss (psi)
                                 TVD = true vertical depth (ft)
	
This enables full wellbore ECD profiling, critical for wellbore stability and drilling optimization.



# Multiple Mud Comparison

The project supports comparative analysis of different drilling fluids:

a) Generate Bingham curves for multiple muds.

b) Compare yield stress and plastic viscosity

c) Support mud selection decisions under high-temperature conditions

d) Visualization outputs provide engineers with clear, actionable insights.



## Why This Matters

By combining mud lab measurements, Bingham Plastic rheology, temperature correction, and hydraulic modeling, this project demonstrates how data science enhances drilling engineering:

a) Reduces modeling errors in HPHT wells.

b) Supports accurate ECD prediction

c) Provides a scalable framework for drilling hydraulics simulations

This repository is the skeleton of a full drilling hydraulics engine, bridging engineering expertise and computational modeling.


*** Author ***

Obua Innocent
Drilling & Completion Fluids Engineer | Data Science Practitioner

Portfolio project demonstrating the application of data science and physics-based modeling to solve real-world drilling fluid challenges in the oil and gas industry.