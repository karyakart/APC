import numpy as np
a=np.array([
        [
            [1,2,3],
            [4,5,6],
        ],
        [
            [7,8,9],
            [10,11,12]
        ]
])
print("array is:\n",a)

print("first 2d block:\n ",a[0])
print("second 2d block:\n",a[1])
print("element of 1st array 2nd row and 3rd coloumn element: ",a[0,1,2])
print("2nd row of 1st block:\n",a[0,1])