import numpy as np
a=int(input("Enter no of rows: "))
b=int(input("Enter no of coloms: "))
array=np.array([[i*j for i in range(a)] for j in range(b)])
print(array)
