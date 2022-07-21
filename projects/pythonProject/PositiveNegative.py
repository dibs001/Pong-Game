i=0
sum=0
while (True):
    n=int(input('Enter a no.:'))
    if (n!=-1):
        sum=sum+n
        i=i+1
    else:
        break
if (i==0):
    print("-1 encountered!")
else:
    print("Average of positive and negative no.s:",(sum/i))