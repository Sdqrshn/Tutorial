names = input("Enter names separated by commas: ").split(",")
names = [name.strip() for name in names]  # Remove extra spaces
names.sort()
print("Sorted names:", ", ".join(names))
