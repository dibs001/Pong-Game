import math
n=int(input("Enter the limit:"))
x=int(input("Enter the no.:"))
sum=0
k=1
for i in range(1,n+1):
    f=1
    for c in range (1,k+1):
        f=f*c
    if (i%2!=0):
        sum=sum+(pow(x,k)/f)
    else:
        sum = sum-(pow(x,k)/f)
    k=k+2
print(f"Sum of series:{sum}")