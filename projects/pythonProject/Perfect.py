n=int(input("Enter the no.:"))
s=0
for i in range(1,(n//2)+1):
    if (n%i==0):
        s=s+i
if (s==n):
    print(f"{n} is a perfect no.!")
else:
    print(f"{n} is not a perfect no.!")