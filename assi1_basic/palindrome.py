num = int(input("Enter a number: "))
on = num
rn = 0

while num > 0:
    digit = num % 10
    rn = rn * 10 + digit
    num //= 10

if on == rn:
    print("it is a palindrome")
else:
    print("it is not a palindrome")
