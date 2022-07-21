i=0
sum=0
while (True):
    i=i+1
    n=int(input("Enter a no.:"))
    sum=sum+n
    if i==10:
        break
print("Sum:",sum)
print("\nAverage:",(sum/10))