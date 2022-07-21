print("Floyd's Triangle-->")
for i in range(0,6):
    for j in range(i,i+i):
        print(j%2,end=" ")
    print()