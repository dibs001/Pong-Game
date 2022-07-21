m=int(input("Enter the lower limit:"))
n=int(input("Enter the upper limit:"))
even=[]
odd=[]
for i in range(m,n+1):
    if (i%2==0):
        even.append(i)
    else:
        odd.append(i)
print("Even no.s:",even)
print("Odd no.s:",odd)