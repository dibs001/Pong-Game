x = int(input("\nEnter a no.:"))
s=0
while (x>0):
    s=(s*10)+(x%10)
    x//=10
print(f"\nReverse is:{s}")