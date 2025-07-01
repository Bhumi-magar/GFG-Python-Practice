#To find if the given user number is a prime number or not
num = int(input("Enter a num: "))
if num <= 1:
    print("It is not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("It isot a prime number")
            break
    else:
        print("It is a prime number")
