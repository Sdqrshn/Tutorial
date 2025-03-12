data = input("Enter mixed data separated by spaces: ").split()
ints = [int(x) for x in data if x.isdigit()]
floats = [float(x) for x in data if '.' in x and x.replace('.', '', 1).isdigit()]
strings = [x for x in data if not x.isdigit() and not x.replace('.', '', 1).isdigit()]
print(f"Integers: {ints}\nFloats: {floats}\nStrings: {strings}")
