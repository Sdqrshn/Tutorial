def fib(n):
    return n if n <= 1 else fib(n-1) + fib(n-2)

n = int(input("Enter n: "))
print(f"{n}th Fibonacci number: {fib(n)}")
