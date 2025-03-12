import math
x = float(input("Enter x in radians: "))
n = int(input("Enter number of terms: "))
sin_x = sum((-1)**i * x**(2*i + 1) / math.factorial(2*i + 1) for i in range(n))
print(f"sin({x}) ≈ {sin_x}")
