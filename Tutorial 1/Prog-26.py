import math
x1, y1 = (float(x) for x in input("Enter x1, y1: ").split()) 
x2, y2 = (float(x) for x in input("Enter x2, y2: ").split())
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"Distance: {distance:.2f}")
