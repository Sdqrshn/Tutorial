low = int(input("Enter lower limit: "))
high = int(input("Enter upper limit: "))
sum_odds = sum(i for i in range(low, high + 1) if i % 2 != 0)
print(f"Sum of odd numbers: {sum_odds}")
