from collections import Counter
nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
mode = Counter(nums).most_common(1)[0][0]
print(f"Mode: {mode}")
