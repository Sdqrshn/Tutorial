num = int(input("Enter a number: "))
sum_of_digits = sum(int(digit) for digit in str(num))
print(f"Sum of digits: {sum_of_digits}")
