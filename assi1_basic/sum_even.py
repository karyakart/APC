sum=0
s=0
add=0
n=int(input("enter any number upto which you want to print:"))
for i in range(1,n):
    add+=i

    if i%2==0:
     sum+=i
    else:
       s+=i
print("total sum if all natural number is:",add)
print("even sum:",sum)
print("odd sum:",s)