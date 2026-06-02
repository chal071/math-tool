import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

# 矩阵加法
print("A + B =")
print(A + B)

# 矩阵乘法（注意！不是 A*B）
print("A × B =")
print(A @ B)

# 转置
print("A 的转置 =")
print(A.T)

# 行列式
det = np.linalg.det(A)
print(f"A 的行列式：{det}")

# 逆矩阵
inv = np.linalg.inv(A)
print("A 的逆矩阵 =")
print(inv)

# 验证：A × A的逆 应该等于单位矩阵
print("A × A⁻¹ =")
print(np.round(A @ inv))   # round 消除浮点误差

# 特征值和特征向量
eigenvalues, eigenvectors = np.linalg.eig(A)

print(f"特征值：{eigenvalues}")
print(f"特征向量：")
print(eigenvectors)

# 验证第一个特征值和特征向量
lambda1 = eigenvalues[0]
v1 = eigenvectors[:, 0]   # 取第一列

print(f"λ₁ = {lambda1:.3f}")
print(f"v₁ = {v1}")
print(f"A × v₁ = {A @ v1}")          # 左边
print(f"λ₁ × v₁ = {lambda1 * v1}")   # 右边
# 两个结果应该相等！