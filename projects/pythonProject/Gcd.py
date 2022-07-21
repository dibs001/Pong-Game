n1=int(input("Enter the  number:"))
n2= int(input("Enter another number:"))
while (n2!=0):
    s=n1%n2
    n1=n2
    n2=s
if n2==0:
    print(n1)
