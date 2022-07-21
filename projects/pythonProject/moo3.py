x = int(input("\nEnter a limit:"))
print("\nThe no.s divisible by 6-->\n")
i=1
while (i<=x):
    if (i%3==0 and i%2==0):
        print(i," ")
    i=i+1
if (x<6):
    print("No numbers are divisible by 6 in the given range")