num = int(input("Enter a number: "))
if num > 1:
    flag = False  
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            flag = True  
            break
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")


