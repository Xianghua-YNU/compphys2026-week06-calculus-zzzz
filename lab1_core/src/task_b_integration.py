import math

def debye_integrand(x: float) -> float:
    if abs(x) < 1e-12:
        return 0.0
    ex = math.exp(x)
    return (x ** 4) * ex / ((ex - 1.0) ** 2)

def trapezoid_composite(f, a: float, b: float, n: int) -> float:
    # TODO B1:实现复合梯形积分
    if n <= 0:
        raise ValueError("分段数n必须为正整数")
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        x_i = a + i * h
        integral += f(x_i)
    integral *= h
    return integral

def simpson_composite(f, a: float, b: float, n: int) -> float:
    # TODO B2:实现复合Simpson积分，检查n为偶数
    if n <= 0:
        raise ValueError("分段数n必须为正整数")
    if n % 2 != 0:
        raise ValueError("复合Simpson积分要求分段数n必须为偶数")
    h = (b - a) / n
    integral = f(a) + f(b)
    # 奇数项系数4
    for i in range(1, n, 2):
        x_i = a + i * h
        integral += 4 * f(x_i)
    # 偶数项系数2
    for i in range(2, n, 2):
        x_i = a + i * h
        integral += 2 * f(x_i)
    integral *= h / 3
    return integral

def debye_integral(T: float, theta_d: float = 428.0, method: str = "simpson", n: int = 200) -> float:
    # TODO B3:计算Debye积分
    if T <= 0:
        raise ValueError("温度T必须大于0")
    x = theta_d / T
    # 选择积分方法
    if method == "trapezoid":
        integral_val = trapezoid_composite(debye_integrand, 0.0, x, n)
    elif method == "simpson":
        integral_val = simpson_composite(debye_integrand, 0.0, x, n)
    else:
        raise ValueError("method仅支持'trapezoid'或'simpson'")
    # 德拜积分公式
    debye_val = 3.0 / (x ** 3) * integral_val
    return debye_val