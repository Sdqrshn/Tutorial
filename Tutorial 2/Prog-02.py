string = input("Enter a string: ")
result = "".join(string[i] for i in range(len(string)) if i % 2 == 0)
print(f"String after removing odd index characters: {result}")
