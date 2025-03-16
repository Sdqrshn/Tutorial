x = int(input("Enter x: "))
y = int(input("Enter y: "))
result = 1
for _ in range(y):
    result *= x
print(f"{x}^{y} = {result}")
