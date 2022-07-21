upper=int(input("Enter the upper limit:"))
lower=int(input("Enter the lower limit:"))
if (upper!=lower):
    print("Palindrome no.s-->")
    for i in range(lower,upper+1):
        s=0
        k=i
        while(k>0):
            s=(s*10)+(k%10)
            k//=10
        if i==s:
            print(i," ")
else:
    print("The upper and lower limits are the same!")