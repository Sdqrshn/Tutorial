nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
nums.sort()
if len(nums) % 2 == 0:
    median = (nums[len(nums) // 2 - 1] + nums[len(nums) // 2]) / 2
else:
    median = nums[len(nums) // 2]
print(f"Median: {median}")
