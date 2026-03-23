# Drillpipe Pressure Loss
import numpy as np

def drillpipe_pressure_loss(mu, velocity, diameter, length):
    """
    Simplified laminar flow pressure loss in drillpipe
    """

    dp = 32 * mu * velocity * length / (diameter ** 2)

    return dp

# Bit Nozzle Pressure Loss
def bit_pressure_loss(flow_rate, mud_density, nozzle_area):

    """
    Pressure drop across bit nozzles
    """

    velocity = flow_rate / nozzle_area

    dp = 0.5 * mud_density * velocity**2

    return dp

# Annular Pressure Loss
def annular_pressure_loss(dp_dz, depth):
    """
    Calculate total annular pressure loss.

    Parameters:
    dp_dz (float): Pressure gradient (Pa/m)
    depth (float): Well depth (m)

    Returns:
    float: Total annular pressure loss (Pa)
    """

    dp_total = dp_dz * depth

    return dp_total


# Total Standpipe Pressure
def standpipe_pressure(dp_pipe, dp_bit, dp_annulus):

    spp = dp_pipe + dp_bit + dp_annulus

    return spp


def bit_hydraulics_pro(flow_rate, mud_density, nozzle_area, Cd=0.95):
    """
    Rig-representative bit hydraulics model.

    Parameters:
    flow_rate (m3/s)
    mud_density (kg/m3)
    nozzle_area (m2) → total nozzle flow area
    Cd (float): discharge coefficient (0.95–0.98)

    Returns:
    dp_bit (Pa), velocity (m/s), hhp (W), impact_force (N)
    """

    # --- Jet velocity ---
    velocity_bit = flow_rate / nozzle_area

    # --- Real orifice pressure drop ---
    dp_bit = (mud_density * velocity_bit**2) / (2 * Cd**2)

    # --- Hydraulic power at bit ---
    hhp_bit = dp_bit * flow_rate

    # --- Impact force (jet momentum transfer) ---
    impact_force_bit = mud_density * flow_rate * velocity_bit

    return dp_bit, velocity_bit, hhp_bit, impact_force_bit



def calculate_ecd(mud_density, cumulative_dp_annulus, depth):
    """
    Calculate ECD using cumulative annular pressure loss.

    Parameters:
    mud_density (kg/m3)
    cumulative_dp_annulus (Pa)
    depth (m)
    
    Returns:
    ecd (ppg)

    # Calculate ECD for all other depths
    # Using your original logic:
    # (dp_annulus/depth) = Pa/m
    # / 6894.76 = psi/m
    # / 3.281 = psi/ft (since 1m = 3.281ft)
    """

    # Base mud weight
    mud_weight_ppg = mud_density / 119.826
    # 1. Handle the surface (depth = 0)
    if depth <= 0:
        return mud_weight_ppg
    
    # Unit conversions
    depth_ft = depth * 3.281
    dp_psi = cumulative_dp_annulus / 6894.76

    # ECD formula
    ecd = mud_weight_ppg + dp_psi / (0.052 * depth_ft)

    return ecd

def reynolds_number(rho, velocity, hydraulic_diameter, mu):

    Re = (rho * velocity * hydraulic_diameter) / mu

    return Re


def friction_multiplier(Re):
    """
    Simple correction for non-laminar effects
    """

    if Re < 2100:
        return 1.0
    elif Re < 4000:
        return 1.5
    else:
        return 2.0
    
