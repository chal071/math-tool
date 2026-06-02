import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)

# 三个函数
y1 = x**2
y2 = x**3
y3 = np.sin(x)      # sin(x)

# 画三条线，每条给不同颜色和标签
plt.plot(x, y1, color="blue",   label="x²")
plt.plot(x, y2, color="red",    label="x³")
plt.plot(x, y3, color="green",  label="sin(x)")

# 标记原点
plt.scatter([0], [0], color="black", zorder=5)
plt.annotate("原点", xy=(0, 0), xytext=(1, -5),
             arrowprops=dict(arrowstyle="->"))

plt.title("多函数对比")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()        # 显示图例
plt.grid(True)
plt.ylim(-10, 10)   # 限制y轴范围，不然x³会太大
plt.show()
