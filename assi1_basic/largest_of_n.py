n = int(input("Enter how many numbers: "))
num = int(input("Enter number 1: "))
largest = num
for i in range(2, n + 1):
    num = int(input(f"Enter number"))
    if num > largest:
        largest = num

print(f"\nThe largest number is:", largest)
