import numpy as np
import math

def rate_3alpha(T: float) -> float:
    T8 = T / 1.0e8
    return 5.09e11 * (T8 ** (-3.0)) * np.exp(-44.027 / T8)

def finite_diff_q_dT(T: float, h: float = 1e-8) -> float:
    # TODO A1:前向差分实现dq/dT
    q_T = rate_3alpha(T)
    q_T_h = rate_3alpha(T + h)
    dq_dT = (q_T_h - q_T) / h
    return dq_dT

def sensitivity_nu(T: float, h: float = 1e-8) -> float:
    # TODO A2:计算温度敏感性指数nu
    q_T = rate_3alpha(T)
    dq_dT = finite_diff_q_dT(T, h)
    nu = (T / q_T) * dq_dT
    return nu

def nu_table(T_values, h: float = 1e-8):
    # TODO A3:返回(T, nu)元组列表
    result = []
    for T in T_values:
        nu_val = sensitivity_nu(T, h)
        result.append((T, nu_val))
    return result