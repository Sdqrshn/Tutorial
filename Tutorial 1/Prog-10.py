n = int(input("Enter number of elements: "))
nums = list(map(int, input("Enter the numbers: ").split()))
sum_even = sum(num for num in nums if num % 2 == 0)
print(f"Sum of even numbers: {sum_even}")
