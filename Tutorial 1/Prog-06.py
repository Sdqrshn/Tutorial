a = float(input("First side"))
b = float(input("Second side "))
c = float(input("Third side"))

sides = sorted([a, b, c])
if sides[0]**2 + sides[1]**2 == sides[2]**2:
    print("Right-angled")
else:
    print("Not right-angled")
