x=int(input("Enter 1st no.:"))
y=int(input("Enter 2nd no.:"))
print("Addition:",x+y)
if (x>y):
    print("Subtraction:",x-y)
    print("Division:",x / y)
else:
    print("Subtraction:", y-x)
    print("Division:", y/x)
print("Multiplication:",x*y)
print(x," to the power ",y,":",x**y)
print(y," to the power ",x,":",y**x)
#swap
z=x
x=y
y=z
print("After swapping:\n1st no:",x,"\n2nd no:",y)