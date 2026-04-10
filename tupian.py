import sys
import os
# ===================== 核心修复：添加模块搜索路径 =====================
# 自动获取当前文件所在的项目根目录
project_root = os.path.dirname(os.path.abspath(__file__))
# 把模块所在的src文件夹加入Python的搜索路径
lab1_src = os.path.join(project_root, "lab1_core", "src")
lab2_src = os.path.join(project_root, "lab2_bonus", "src")
sys.path.append(lab1_src)
sys.path.append(lab2_src)
# ======================================================================

import numpy as np
import matplotlib.pyplot as plt
from task_c_ring_potential import ring_potential_grid
from bonus_plate_gravity import force_curve

# ========== 1. 生成Task C 带电圆环等势线图 ==========
print("正在生成带电圆环等势线图...")
# 网格设置
y_min, y_max = -2.0, 2.0
z_min, z_max = -2.0, 2.0
ny, nz = 200, 200
y_grid = np.linspace(y_min, y_max, ny)
z_grid = np.linspace(z_min, z_max, nz)

# 计算电势矩阵
V = ring_potential_grid(y_grid, z_grid, x0=0.0, a=1.0, q=1.0, n_phi=720)

# 绘图
plt.figure(figsize=(8, 6), dpi=300)
Y, Z = np.meshgrid(y_grid, z_grid)
levels = np.linspace(0.2, 2.0, 20)
# 绘制等势线
contour = plt.contour(Y, Z, V, levels=levels, cmap='viridis', linewidths=0.8)
plt.contourf(Y, Z, V, levels=levels, cmap='viridis', alpha=0.7)
# 标注圆环位置
plt.scatter([-1, 1], [0, 0], color='red', s=20, label='带电圆环')
# 格式设置
plt.xlabel('y (m)', fontsize=10)
plt.ylabel('z (m)', fontsize=10)
plt.title('带电圆环yz平面等势线分布 (x=0)', fontsize=12)
plt.colorbar(label='电势 (V)')
plt.legend()
plt.grid(alpha=0.3, linestyle='--')
plt.axis('equal')
# 保存图片
plt.savefig('./ring_potential_contour.png', bbox_inches='tight')
plt.close()
print("等势线图已保存为 ring_potential_contour.png")

# ========== 2. 生成Bonus 方板引力曲线图 ==========
print("正在生成方板引力曲线图...")
z_values = np.linspace(0.2, 20.0, 100)
Fz_values = force_curve(z_values)

# 绘图
plt.figure(figsize=(8, 6), dpi=300)
plt.plot(z_values, np.abs(Fz_values), color='blue', linewidth=1.5, label='数值计算结果')
# 远场点引力近似
G = 6.674e-11
F_point = G * 1.0e4 * 1.0 / (z_values ** 2)
plt.plot(z_values, F_point, color='red', linestyle='--', linewidth=1.2, label='远场点引力近似')
# 格式设置
plt.xlabel('z (m)', fontsize=10)
plt.ylabel('|Fz| (N)', fontsize=10)
plt.title('方板中心正上方引力大小随z的变化', fontsize=12)
plt.yscale('log')
plt.legend()
plt.grid(alpha=0.3, linestyle='--')
# 保存图片
plt.savefig('./plate_force_curve.png', bbox_inches='tight')
plt.close()
print("引力曲线图已保存为 plate_force_curve.png")

print("所有图片生成完成！")