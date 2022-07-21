import re
txt = input("Enter string:")
x = re.findall("wo.+d", txt)
print(x)

