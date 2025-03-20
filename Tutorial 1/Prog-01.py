s = int(input("Enter time in seconds: "))
h = s // 3600
m = (s % 3600) // 60
s = s % 60
print(f"{h:02}:{m:02}:{s:02}")
