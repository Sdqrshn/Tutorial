num = int(input("Enter a number: "))
n = len(str(num))
sum_digits = sum(int(digit) ** n for digit in str(num))
print(f"{num} is an Armstrong number" if sum_digits == num else f"{num} is not an Armstrong number")
