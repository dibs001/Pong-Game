# Write a Python program to evaluate the X^Y, where X and Y are both integers.
X=int(input("Enter an integer no.:"))
Y=int(input("\nEnter another integer:"))
print("\n",X," ^ ",Y,":",(X**Y))
# Write a Python program to find the circumference and area of a circle.
r=float(input("\nEnter the radius of a circle:"))
print("\nArea of circle:",(3.14*r*r),"\nCircumference of circle:",(2*3.14*r))
#to check whether a no. is odd or even
no=int(input("\nEnter a no.:"))
if (no%2==0):
    print("\n",no," is even!")
else:
    print("\n",no," is odd!")
#to find max value among 3 entered values
x=int(input("\nEnter 1st no.:"))
y=int(input("\nEnter 2nd no.:"))
z=int(input("\nEnter 3rd no.:"))
if (x>y and x>z):
    print("\n",x," has max value!")
elif (y>x and y>z):
    print("\n",y," has max value!")
elif (z>y and z>x):
    print("\n",z," has max value!")
# to check whether a no. is positive or negative
x=int(input("\nEnter a no.:"))
if (x>0):
    print("\n",x," is positive!")
elif (x<0):
    print("\n",x, " is negative!")
else:
    print("\n",x, " is neither positive or negative!")
# to check whether a no. is between 1 to 10
x=int(input("\nEnter a no.:"))
if (x>=1 and x<=10):
    print("\n",x," is between 1 to 10!")
else:
    print("\n",x, " is not in the range!")
#to accept an integer (n) between 1 to 9 and computes the value of n+nn+nnn.
n=int(input("\nEnter an integer.:"))
print(n,"+",(n+n*10),"+",(n+n*10+n*100),":",(n+(n+n*10)+(n+n*10+n*100)))
# to return true if the two given integer values are equal or their sum or difference is 5.
a=int(input("\nEnter 1st no.:"))
b=int(input("\nEnter 2nd no.:"))
if ((a-b)==5 or (b-a)==5 or (b+a)==5 or (b==a)):
    print("\nTrue!")
else:
    print("\nFalse!")
#to determine whether the character entered is a vowel or not.
x=input("\nEnter a character:")
if x.lower() in ('a', 'e', 'i', 'o', 'u'):
    print("\n",x," is Vowel!")
elif l.upper() in ('A', 'E', 'I', 'O', 'U'):
    print("\n",x," is Vowel!")
else:
  print("\n",x," is Consonant!")
# to determine whether a year is leap year or not
year=int(input("\nEnter a year:"))
if((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):
    print("\n",year," is a leap Year!")
else:
    print("\n",year, " is not a leap Year!")