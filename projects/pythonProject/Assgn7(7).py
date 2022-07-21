str=input("Enter a string:")
flag=False
for char in str:
    if char in " !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~":
        flag=True
        break
if flag==True:
    print(f"Special character is present in \"{str}\"")
else:
    print(f"Special characters are not present in \"{str}\"")
