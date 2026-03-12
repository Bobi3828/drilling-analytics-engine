# Week 2: Bingham Plastic Rheology Model

## Problem

Drilling fluids exhibit non-Newtonian flow behavior that cannot be accurately described using Newtonian viscosity models.

The Bingham Plastic model is commonly used in drilling hydraulics to represent fluids with yield stress and linear shear-rate behavior.

## Model

τ = τ0 + μp γ

Where:
τ = shear stress
τ0 = yield stress
μp = plastic viscosity
γ = shear rate

## Engineering Importance

The Bingham Plastic model forms the basis for pressure loss calculations in many drilling hydraulics correlations.

This module provides a computational implementation of the model and visualization of shear stress vs shear rate behavior.

## Viscometer Data Integration

Field viscometer readings (θ600 and θ300) are used to compute Bingham Plastic parameters.

               PV = θ600 − θ300, field units (centipoise, cP)
               YP = θ300 − PV, field units (lb/100ft²)

These parameters are converted into SI units and used to generate rheology curves representing drilling fluid behavior.

  ### convert_yp_to_pascal(YP)..........Pascals (Pa)
This formula converts the Yield Point (YP) from field units (lb/100ft²) to the SI unit of stress, Pascals (Pa).
The Math: 
                       1 lb/100ft² ~ 0.4788 Pa.
Purpose: Yield stress represents the minimum stress required to make the fluid move. Converting to Pascals allows for standardized hydraulic calculations and pressure drop modeling.

  ### plastic_viscosity = PV / 1000 .........Pascal-seconds (Pa·s)
This formula converts the Plastic Viscosity (PV) from field units (centipoise, cP) to Pascal-seconds (Pa·s). 
The Math: 
                  1 centipoise ~ 0.001 Pascal-seconds. Dividing by 1,000 performs this decimal shift.
Purpose: PV represents the resistance to flow caused by mechanical friction between solids and liquids in the fluid. Using Pa·s is necessary when working in consistent MKS (meter-kilogram-second) units. 

Your model now reflects actual mud lab workflow:

Viscometer readings
        ↓
PV and YP
        ↓
Yield stress + plastic viscosity
        ↓
Bingham rheology curve

## Multiple Mud Comparison

This analysis computes Bingham parameters for several drilling fluids based on viscometer readings (θ600, θ300). 

Each mud's shear stress curve is generated using:

                    τ = τ0 + μp * γ

                    where τ0 = yield stress (Pa), μp = plastic viscosity (Pa.s), γ = shear rate (1/s).


Comparative curves allow engineers to:

- Select muds based on downhole rheology
- Visualize differences in yield stress and plastic viscosity
- Build foundation for mud selection decision tools

Temperature-Corrected Rheology

Surface viscometer measurements are corrected for downhole temperature using an Arrhenius-based viscosity correction.

This provides more realistic rheological behavior for drilling fluids under high-temperature well conditions.


Your system now has a real engineering workflow:

                          Viscometer data
                                ↓
                             PV / YP
                                ↓
                      Bingham rheology model
                                ↓
                     Temperature correction
                                ↓
                     Downhole rheology curves

That is the beginning of a real drilling hydraulics engine.

## A computational workflow.
Your project can now simulate:

                              Viscometer data
                                     ↓
                                  PV / YP
                                     ↓
                              Bingham rheology
                                     ↓
                         Temperature correction
                                     ↓
                             Downhole rheology
                                     ↓
                           Annular pressure loss

This is now a real drilling hydraulics chain.



## Objective: Compute ECD from annular pressure loss.
The simplified relationship is:

ECD = MW + (ΔP / (0.052 × TVD))

Where:

                           MW  = mud weight (ppg)
                           ΔP  = annular pressure loss (psi)
                           TVD = true vertical depth (ft)

Right now your hydraulics model gives pressure gradient in Pa/m, so we convert units first. Engineering is mostly unit conversion disguised as intelligence.


Your System Can Now Simulate a full drilling hydraulics chain:

                                    Viscometer data
                                           ↓
                                        PV / YP
                                           ↓
                                    Bingham rheology
                                           ↓
                                  Temperature correction
                                           ↓
                                   Downhole rheology
                                           ↓
                                   Annular pressure loss
                                           ↓
                               Equivalent Circulating Density

At this point your repository is no longer a toy. It is the skeleton of a drilling hydraulics engine.


Your repo now simulates a full drilling hydraulics workflow:

                                      Viscometer data
                                            ↓
                                         PV / YP
                                            ↓
                                     Bingham rheology
                                            ↓
                                  Temperature correction
                                            ↓
                                   Annular pressure loss
                                            ↓
                                     ECD calculation
                                            ↓
                                     ECD depth profile