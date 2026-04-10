import numpy as np

def ring_potential_point(x: float, y: float, z: float, a: float = 1.0, q: float = 1.0, n_phi: int = 720) -> float:
    # TODO C1:离散积分计算单点电势
    # 圆环离散为n_phi个电荷元，圆心在原点，位于xy平面
    phi = np.linspace(0, 2 * np.pi, n_phi, endpoint=False)
    x_ring = a * np.cos(phi)
    y_ring = a * np.sin(phi)
    # 计算目标点到电荷元的距离
    r = np.sqrt((x - x_ring) ** 2 + (y - y_ring) ** 2 + z ** 2)
    # 奇点截断，避免除以0
    r[r < 1e-12] = 1e-12
    # 标量电势叠加
    potential = q / n_phi * np.sum(1.0 / r)
    return potential

def ring_potential_grid(y_grid, z_grid, x0: float = 0.0, a: float = 1.0, q: float = 1.0, n_phi: int = 720):
    # TODO C2:计算yz网格电势矩阵
    ny = len(y_grid)
    nz = len(z_grid)
    V = np.zeros((nz, ny))
    # 遍历网格计算电势
    for i, z in enumerate(z_grid):
        for j, y in enumerate(y_grid):
            V[i, j] = ring_potential_point(x0, y, z, a, q, n_phi)
    return V

def axis_potential_analytic(z: float, a: float = 1.0, q: float = 1.0) -> float:
    return q / np.sqrt(a * a + z * z)