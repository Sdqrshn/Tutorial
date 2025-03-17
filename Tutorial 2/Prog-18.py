def f(n):
    return n if n <= 1 else f(n-1) + f(n-2)

n = int(input("Enter n: "))
print(f"{n}th Fibonacci number: {f(n)}")
