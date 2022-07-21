str=input("Enter a string with ',' or '.':")
s=""
for c in str:
    if c==',':
        s=s+'.'
    elif c=='.':
        s=s+','
    else:
        s=s+c
print("The modified string:",s)