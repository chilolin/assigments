import numpy as np

a = np.array([-1, -2, -3])
x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([[7, 8, 9], [-1, -2, -3]])
z = np.array([[1, 2], [3, 4], [5, 6]])

# 加算
print(a + x)
print(x + y)
# 引算
print(x - y)
# スカラー倍
print(3 * x)
# 行列の積
print(np.dot(x, z))
