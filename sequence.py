#The Fibonaci sequence
num = int(input("Enter num:  "))

if num == 0:
    print(1)
elif num == 1:
    print(1, 1)
else:
    print(1, 1, end=" ")
    a = 1
    b = 1
    for i in range(2, num + 1):
        c = a + b
        print(c, end=" ")
        a = b
        b = c
