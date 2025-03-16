for num in range(100, 1001):
    sumofdigits = sum(int(digit) for digit in str(num)) 
    if sumofdigits % 9 == 0:
        print(num, end=" ")
print()
