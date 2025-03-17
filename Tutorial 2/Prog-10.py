import re
def is_valid_password(password):
    return (len(password) >= 6 and
            re.search("[a-z]", password) and
            re.search("[0-9]", password) and
            re.search("[A-Z]", password) and
            re.search("[$#@]", password))

password = input("Enter password: ")
if is_valid_password(password):
    print("Valid password")
else:
    print("Invalid password")
