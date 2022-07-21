str=input("Enter a string:")
v=0
for char in str:
    if char in "aeiou":
        v=v+1
if v!=0:
    print(f"\"{str}\" has {v} vowels in it!")
else:
    print(f"{str} has no vowels in it!")
