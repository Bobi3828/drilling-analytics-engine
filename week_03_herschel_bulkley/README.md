Week 3: Herschel–Bulkley Rheology Model

Drilling fluids often exhibit non-linear shear-rate behaviour
that cannot be accurately captured by the Bingham model.

The Herschel–Bulkley model introduces a flow behaviour index
that captures shear thinning effects.

τ = τy + K γⁿ

Where:
τy = yield stress
K  = consistency index
n  = flow behaviour index


Up to now you computed ECD at one depth. Real wells don’t behave like that. Temperature, rheology, and pressure losses all evolve with depth.

So we now simulate the full chain which finally gives you something that looks like a real hydraulics profile.:
depth
 ↓
temperature profile
 ↓
K(T)
 ↓
HB rheology
 ↓
apparent viscosity
 ↓
pressure gradient
 ↓
ECD profile

Plot ECD vs Depth: Your curve should now increase gradually with depth, not remain a straight line like earlier.

That happens because:

temperature ↑
↓
K ↓
↓
viscosity ↓
↓
pressure loss ↓

But hydrostatic pressure dominates, so ECD still increases slightly.

What You Just Built

Your simulator now models a dynamic wellbore:

depth
temperature
rheology change
hydraulics change
ECD change

Which is exactly the physics chain used in drilling hydraulics programs.

Now you should see two different curves.

Usually:

Bingham → higher ECD
HB → lower ECD

Because Bingham overestimates viscosity at high shear rates.