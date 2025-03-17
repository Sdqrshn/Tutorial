def evenodd(n):
    print("Even" if n % 2 == 0 else "Odd")

def sign(n):
    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")

def factors(n):
    print([i for i in range(1, n + 1) if n % i == 0])

choice = int(input("1. Even or Odd ?\n2. Sign ?\n3. Factors ?\nEnter choice: "))
num = int(input("Enter number: "))

if choice == 1:
    evenodd(num)
elif choice == 2:
    sign(num)
elif choice == 3:
    factors(num)
else:
    print("Invalid choice")
