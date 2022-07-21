n=int(input("Enter the limit:"))
s=0
for i in range(1,n+1):
    f=1
    for c in range (1,i+1):
        f=f*c
    s=s+(i/f)
print(f"Sum of series:{s}")