import numpy as np

A = eval(input("Enter Array: "))
A = np.array(A)
print(np.inner(np.transpose(A),A[:,0]))
