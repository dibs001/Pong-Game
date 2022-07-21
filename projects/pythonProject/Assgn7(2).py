import re
str=input("Enter a string:")
x = re.findall("he.*o", str)
print(x)
