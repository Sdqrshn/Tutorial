num = [int(input(f"Enter number {i+1}: ")) for i in range(4)]
p = [n for n in nums if n > 0]
n = [n for n in nums if n < 0]
print(f"Sum of positive nos: {sum(p)}, Average: {sum(p)/len(p) if p else 0}")
print(f"Sum of negative nos: {sum(n)}, Average: {sum(n)/len(n) if n else 0}")
