n=int(input("Enter the limit:"))
s=0
for i in range(1,n+1):
    s=s+(1/i)
print(f"Sum of series:{s}")