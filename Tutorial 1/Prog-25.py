x = int(input("Enter base: "))
y = int(input("Enter exponent: "))
result = 1
for _ in range(y):
    result *= x
print(f"{x}^{y} = {result}")
