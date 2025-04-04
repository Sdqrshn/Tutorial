import numpy as np
a = np.random.randint(0, 21, size=(3, 3))
b = np.random.randint(0, 21, size=(3, 3))
print("Array A:")
print(a)
print("Array B:")
print(b)
add = a + b
print("Addition:")
print(add)
product = np.dot(a, b)
print("Multiplication:")
print(product)
transpose = product.T
print("Transpose:")
print(transpose)
