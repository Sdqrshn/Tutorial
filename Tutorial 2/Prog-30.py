nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
unique_nums = [num for num in nums if nums.count(num) == 1]
print(f"List after completely removing duplicates: {unique_nums}")
