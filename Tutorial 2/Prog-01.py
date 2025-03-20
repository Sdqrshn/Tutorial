string = input("Enter a string: ")  
vowels = "aeiouAEIOU"  
result = ""  
for char in string:    
    if char not in vowels:    
        result += char    
print(f"String without vowels: {result}")
