string = input("Enter a string: ")
is_palindrome = True
n = len(string)
for i in range(n // 2):
    if string[i] != string[n - i - 1]:
        is_palindrome = False
        break
print("Palindrome" if is_palindrome else "Not a palindrome")
