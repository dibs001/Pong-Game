n=int(input("Enter the no.:"))
s=0
while (n>0):
    s=(s*10)+(n%10)
    n//=10
print(f"Reverse of {n}:{s}")