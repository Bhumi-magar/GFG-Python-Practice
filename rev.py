#Reverse triangle
n=int(input("Enter n: "))
for i in range(n):
    for j in range (n-i):
        print("*", end=" ")
    print()