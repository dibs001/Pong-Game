str=input("Enter a string with ',' or '.':")
ch=int(input("Enter a choice:\n1.To replace ',' with '.' \n2.To replace '.' with ','\n"))
if ch==1:
    if ',' in str:
        str=str.replace(',','.')
elif ch==2:
    if '.' in str:
        str=str.replace('.', ',')
print("The modified string:",str)