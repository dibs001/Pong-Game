n=int(input("Enter a no.:"))
s=0
k=n
while (n!=0):
    s=s+(n%10)
    n//=10
print(f"\nSum of digits of {k}:",s)