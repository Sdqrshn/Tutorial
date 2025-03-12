string = input("Enter a string: ")
mid = len(string) // 2
result = string[:mid][::-1] + string[mid:][::-1]
print(f"Reversed halves: {result}")
