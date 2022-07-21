upper=int(input("Enter the upper limit:"))
lower=int(input("Enter the lower limit:"))
sum=0
for i in range(lower,upper+1):
    if (i%2==0):
        sum=sum+(i*i)
print(f"Sum of squares of even no.s in the range {lower} and {upper}:{sum}")