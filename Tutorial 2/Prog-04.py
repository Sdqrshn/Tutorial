string = input("Enter string: ")
if " " in string:
    result = string.replace(" ", "*")
else:
    result = f"S{string}S"
print(f"Result: {result}")
