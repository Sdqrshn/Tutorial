n = int(input("Enter number of elements: "))
nums = [int(x) for x in input("Enter the numbers: ").split()]
even = sum(1 for num in nums if num % 2 == 0)
odd = n - even
print(f"Even numbers: {even}, Odd numbers: {odd}")
