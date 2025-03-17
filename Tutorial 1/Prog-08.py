num = int(input("Enter a number: "))
sumofdigits = sum(int(digit) for digit in str(num))
print(f"Sum of digits: {sumofdigits}")
