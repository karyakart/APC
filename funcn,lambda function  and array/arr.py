import array

arr=array.array('i',[10,30,40,20,30,40,50])
print(arr)

#i=typecode for integer values in the array
arr.append(100)
print(arr)

arr.remove(20)
print(arr)

arr.reverse()
print(arr)

print(arr.count(30))

print(arr.buffer_info())