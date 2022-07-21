check1=['Today','Our','Exam','is','over']
check2=check1
check3=check1[:]
check2[0]='Python'
check3[1]='MCQEXAM'
count=0
for c in (check1,check2,check3):
    if c[0]=='Python':
        count+=1
    if c[1]=='MCQEXAM':
        count+=2
print(count)
print(print(print("Hello")))
a='1 2'
print(a*2)
print(a*0)
