import math

def calculate_nCr(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

n = int(input("Enter n: "))
r = int(input("Enter r: "))
result = calculate_nCr(n, r)
print(f"nCr = {result}")
