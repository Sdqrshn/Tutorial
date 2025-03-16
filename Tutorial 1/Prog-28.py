a = int(input("Enter lower limit: "))
b = int(input("Enter upper limit: "))
oddsum = sum(i for i in range(a, b + 1) if i % 2 != 0)
print(f"Sum of odd numbers: {oddsum}")
