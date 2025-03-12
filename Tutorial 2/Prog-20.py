nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
even_sum = sum(num for num in nums if num % 2 == 0)
print(f"Sum of even numbers: {even_sum}")
