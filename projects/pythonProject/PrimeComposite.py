n=int(input("Enter a no. "))
c=0
for i in range(1,n):
    if (n%i==0):
        c=c+1
if (n==1):
    print(f"{n} is neither prime nor composite!")
else:
    if (c==1):
        print(f"{n} is prime!")
    else:
        print(f"{n} is composite!")