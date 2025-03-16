n = int(input("Enter number of elements: "))
nums = []
for _ in range(n):
    nums.append(int(input("Enter a number: "))) 
evensum = sum(num for num in nums if num % 2 == 0)
print(f"Sum of even numbers: {evensum)
