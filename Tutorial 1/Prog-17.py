n = int(input("Enter the range for multiplication tables: "))
for i in range(1, n + 1):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
    print()
