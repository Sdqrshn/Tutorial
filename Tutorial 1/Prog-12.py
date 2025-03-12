nums = [int(input(f"Enter number {i+1}: ")) for i in range(4)]
pos = [n for n in nums if n > 0]
neg = [n for n in nums if n < 0]
print(f"Sum of positive numbers: {sum(pos)}, Average: {sum(pos)/len(pos) if pos else 0}")
print(f"Sum of negative numbers: {sum(neg)}, Average: {sum(neg)/len(neg) if neg else 0}")
