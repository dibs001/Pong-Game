n=int(input("Enter the limit:"))
z= 2 * n - 2
for i in range(0, n):
    for j in range(0, z):
        print(end=" ")
    z = z- 2
    for j in range(0, i + 1):
        print("* ", end="")
    print("\r")