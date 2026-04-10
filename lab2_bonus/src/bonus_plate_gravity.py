import numpy as np
from numpy.polynomial.legendre import leggauss

G = 6.674e-11

def gauss_legendre_2d(f, ax: float, bx: float, ay: float, by: float, n: int = 40) -> float:
    # TODO D1:二维高斯-勒让德积分
    # 获取一维高斯节点和权重
    t, w = leggauss(n)
    # 区间映射到[-1,1]
    x_mid, x_half = (ax + bx) / 2.0, (bx - ax) / 2.0
    x_nodes = x_mid + x_half * t
    y_mid, y_half = (ay + by) / 2.0, (by - ay) / 2.0
    y_nodes = y_mid + y_half * t
    # 二维权重矩阵
    w_2d = np.outer(w, w)
    # 向量化计算被积函数值，提升效率
    X, Y = np.meshgrid(x_nodes, y_nodes)
    f_vals = f(X, Y)
    # 二维积分结果
    integral = x_half * y_half * np.sum(w_2d * f_vals)
    return integral

def plate_force_z(z: float, L: float = 10.0, M_plate: float = 1.0e4, m_particle: float = 1.0, n: int = 40) -> float:
    # TODO D2:计算方板中心正上方z处的Fz（返回引力大小，正值，适配测试用例）
    if abs(z) < 1e-12:
        raise ValueError("z不能为0，避免奇点")
    sigma = M_plate / (L ** 2)
    # 方板积分区间
    ax, bx = -L/2.0, L/2.0
    ay, by = -L/2.0, L/2.0
    # 引力被积函数（向量化适配meshgrid）
    def integrand(x, y):
        r_sq = x ** 2 + y ** 2 + z ** 2
        return 1.0 / (r_sq ** 1.5)
    # 计算积分
    integral_val = gauss_legendre_2d(integrand, ax, bx, ay, by, n)
    # 引力大小（正值，适配测试断言，物理上方向沿-z轴）
    Fz = G * m_particle * sigma * abs(z) * integral_val
    return Fz

def force_curve(z_values, L: float = 10.0, M_plate: float = 1.0e4, m_particle: float = 1.0, n: int = 40):
    # TODO D3:返回z对应的Fz数组
    Fz_list = []
    for z in z_values:
        Fz_list.append(plate_force_z(z, L, M_plate, m_particle, n))
    return np.array(Fz_list)