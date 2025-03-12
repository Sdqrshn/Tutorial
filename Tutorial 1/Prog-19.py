n = int(input("Enter number of elements: "))
nums = list(map(int, input("Enter the numbers: ").split()))
even_count = sum(1 for num in nums if num % 2 == 0)
odd_count = n - even_count
print(f"Even numbers: {even_count}, Odd numbers: {odd_count}")
