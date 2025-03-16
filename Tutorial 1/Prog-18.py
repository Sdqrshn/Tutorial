num = int(input("Enter a number: "))
n = len(str(num))
sumofdigits = sum(int(digit) ** n for digit in str(num))
print(f"{num} is an Armstrong number" if sumofdigits == num else f"{num} isn't an Armstrong number")
