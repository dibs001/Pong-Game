upper=int(input("Enter the upper limit:"))
lower=int(input("Enter the lower limit:"))
if (upper!=lower):
    print("Prime no.s-->")
    for i in range(lower,upper+1):
        c=0
        k=1
        while(k<=i):
            if (i%k==0):
                c=c+1
            k=k+1
        if (c==2):
            print(i," ")
else:
    print("The upper and lower limits are the same!")