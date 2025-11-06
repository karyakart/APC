n = int(input("Enter how many numbers: "))
num = int(input("Enter number 1: "))
smallest = num

for i in range(2, n + 1):
    num = int(input(f"Enter number"))
    if num < smallest:
        smallest = num

print(f"\nThe smallest number is:",smallest)
