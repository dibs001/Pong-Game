print("Python Program to Print a Calendar With Start With Input Day\n\n")
day=int(input("Enter Total Numbers of Days in a Month : "))
firstday=int(input("\n\nEnter First Day Start From Sunday and<0-Sun....5-Sat & 6-Sat> End With Saturday : "))
print('\n\t\tSun \tMon \tTue \tWed \tThu \tFri \tSat \n\n')
for i in range(0,firstday):
    print("\t\t",end="")
for i in range(1,day+1):
    print("\t\t",i,end="")
    if ((firstday+i)%7==0):
        print("\n")