import math
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

d = b**2 - 4*a*c

if d > 0:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print(f"Roots are real and different: {root1}, {root2}")
elif d == 0:
    root = -b / (2*a)
    print(f"Roots are real and the same: {root}")
else:
    real = -b / (2*a)
    imag = math.sqrt(-d) / (2*a)
    print(f"Roots are complex: {real} ± {imag}i")
