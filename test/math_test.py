import sympy as sp

# 定义数学变量 x
x = sp.Symbol('x')

# 定义函数
f = x**3 - 2*x**2 + x

# 求导
derivative = sp.diff(f, x)
print(f"f(x) = {f}")
print(f"f'(x) = {derivative}")

# 积分
integral = sp.integrate(f, x)
print(f"∫f(x)dx = {integral}")

# 求解方程 f(x) = 0
solutions = sp.solve(f, x)
print(f"f(x)=0 的解：{solutions}")

# 计算 f(x) 从 0 到 2 的定积分
result = sp.integrate(f, (x, 0, 2))
print(f"定积分结果：{result}")

# 计算 sin(x)/x 当 x→0 的极限
g = sp.sin(x) / x
limit = sp.limit(g, x, 0)
print(f"极限结果：{limit}")