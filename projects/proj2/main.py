"""dictionary={"Jan":"January","Feb":"February","Mar":"March","Apr":"April","May":"May"}
print(dictionary["Jan"])
# print(dictionary["Jun"])
print(dictionary.get("Jun","Not present!"))"""
'''
i=1
while i<10:
    print(i)
    i+=1
word="Giraffe"
wd=input("Enter a word to check:")

while wd!=word:
    if wd
    print("not found.")'''
'''for letter in "Umbrella Academy":
    print(letter)
friends=["Jim","Pam","Michael"]
for name in friends:
    print(name)
for index in range(2,10):
    print(index)
for index in range(10):
    print(index)
for index in range(len(friends)):
    print(friends[index])
'''
'''no_grid=[[1,2,3],[2,3,4],[4,5,6],[0]]
print(no_grid[3][0])
for row in no_grid:
    print(row)
for row in no_grid:
    for col in row:
        print(col)'''
'''def translate(word):
    trans=""
    for letter in word:
        if letter in "AEIOUaeiou":
            trans=trans+"g"
        else:
            trans=trans+letter
    return trans
print(translate(input("Enter a word:")))
'''
'''
try:
    no=int(input("Enter a no.:"))
    print(no)
    value=no/0
except ZeroDivisionError:
    print("Divided by 0")
except ValueError as err1:
    print((err1))
except ValueError:
    print("Invalid input")
except ZeroDivisionError as err:
    print(err)
'''
'''mainFile=open("emp.file","r")
print(mainFile.readable())
# print(mainFile.readline())
# print(mainFile.readlines()[1])
# print(mainFile.readlines())
for emp in mainFile.readlines():
    print(emp)
# print(mainFile.read())
mainFile.close()'''
''''# empfile=open("emp.file","a")
# empfile.write("\nKelly-->Customer Service")
# empfile.close()'''
'''empfile=open("emp.file1","w")
empfile.write("Hello World")
empfile.write("\nThis is overriding")
empfile.close()'''
