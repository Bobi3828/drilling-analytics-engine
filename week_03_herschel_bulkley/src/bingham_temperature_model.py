import numpy as np

def temperature_corrected_pv(PV_surface, T_surface, T_downhole, alpha=0.01):

    delta_T = T_downhole - T_surface

    PV_T = PV_surface * np.exp(-alpha * delta_T)

    return PV_T


def temperature_corrected_yp(YP_surface, T_surface, T_downhole, beta=0.005):

    delta_T = T_downhole - T_surface

    YP_T = YP_surface * (1 - beta * delta_T)

    return max(YP_T, 0)