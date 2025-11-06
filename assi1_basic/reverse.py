num = int(input("Enter a number: "))
on = num
rn = 0
while num > 0:
    digit = num % 10
    rn = rn * 10 + digit
    num //= 10

print("Reversed number is", rn)

