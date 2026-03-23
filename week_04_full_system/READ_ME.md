Week 4 is where things stop being “annulus-only thinking” and start resembling an actual drilling system.

Up to now you’ve been modeling:

annulus → pressure loss → ECD

Which is only half the story.

Real rigs care about:

pump → drillpipe → bit → annulus → surface

That full loop determines Standpipe Pressure (SPP).

And SPP is what engineers actually monitor in real time.

WEEK 4 — DAY 1
Objective: Build Full Circulation Pressure Model (SPP Foundation)

You are now modeling:

Total Pressure =
Drillpipe Loss
+ Bit Nozzle Loss
+ Annular Loss

This becomes:

Standpipe Pressure (SPP)

Your simulator now models:

pump → drillpipe → bit → annulus → surface pressure

That is literally the core of drilling hydraulics software.

Why This Matters (Real World)

On a real rig:

SPP increase → possible cuttings loading or viscosity increase

SPP drop → possible washout or losses

abnormal trend → early kick detection

So SPP is not just a number.

It’s a diagnostic signal for well health.

What Happens Next

Week 4 will expand this into:

depth-based SPP profiles

pump rate vs SPP sensitivity

bit optimization

eventually ML-based pressure prediction

Quiet reality check.

You now have:

rheology engine

hydraulics engine

ECD model

full circulation pressure model

WEEK 4 — DAY 1
Objective: Build Full Circulation Pressure Model (SPP Foundation)
You are now modeling:
Total Pressure = Drillpipe Loss+bit nozzle loss+annular loss
This becomes:
Standpipe Pressure (SPP)

WEEK 4 — DAY 2
Objective: Depth-Based Standpipe Pressure (SPP) Profile
Yesterday you computed SPP at one depth.
Today you simulate:
SPP vs depth
Which is what real drilling engineers actually monitor.

You now simulate:

depth → temperature → rheology → full circulation → SPP profile

And not just total pressure, but:

where pressure is lost in the system

You now have:

full rheology engine

full hydraulics engine

full circulation system

depth-based SPP

You’re no longer building pieces.

You’re building a drilling simulator.

What You Should Observe
flow rate ↑
→ velocity ↑
→ pressure losses ↑
→ SPP ↑

But:

shear-thinning ↓ viscosity

So the curve is not perfectly linear.

That non-linearity is where real insight lives.

You now understand:

small nozzles → high velocity → high dp → may choke system
large nozzles → low velocity → poor cleaning
optimal → max energy at bit

This is not academic.

This is:

ROP optimization
bit cleaning efficiency
hole cleaning performance
Where Most People Get This Wrong

They think:

higher pressure = better drilling

Wrong.

What matters is:

energy delivered at the bit (HHP)

Objective: Bit Nozzle Optimization (Hydraulic Efficiency)

Right now your bit model is… let’s be honest… too polite:

dp_bit = 0.5 * rho * v^2

That’s fine for a classroom. Not fine for a rig.

Today you will:

1. Model nozzle velocity properly
2. Compute hydraulic horsepower (HHP)
3. Optimize nozzle area for max efficiency