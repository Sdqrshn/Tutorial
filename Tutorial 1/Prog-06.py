a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

sides = sorted([a, b, c])
if sides[0]**2 + sides[1]**2 == sides[2]**2:
    print("The triangle is a right-angled triangle")
else:
    print("The triangle is not a right-angled triangle")
