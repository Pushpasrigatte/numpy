import numpy as np

a=np.arange(1,10)
print(a)

reshaped=a.reshape((3,3))
print(reshaped)
print("Element at (1,1):",reshaped[1,1])

linear=reshaped.flatten()
print(linear)