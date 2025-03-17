nums = [int(num) for num in input("Enter numbers: ").split()]
evensum = sum(num for num in nums if num % 2 == 0)
print(f"Sum of even numbers: {evensum}")
