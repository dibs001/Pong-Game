import math
n=int(input("Enter a no.:"))
k=n
s=0
while (n!=0):
    n%10
    s=s+pow(n%10,3)
    n//=10
if (s==k):
    print("Armstrong no.!")
else:
    print("Not an Armstrong no.!")