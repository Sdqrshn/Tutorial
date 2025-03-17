string = input("Enter a string: ")
palindrome = True
n = len(string)
for i in range(n // 2):
    if string[i] != string[n - i - 1]:
        palindrome = False
        break
print("Palindrome" if palindrome else "Not palindrome")
