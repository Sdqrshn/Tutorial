string = input("Enter a string: ")
x = len(string) // 2
result = string[:x][::-1] + string[x:][::-1]
print(f"Result: {result}")
