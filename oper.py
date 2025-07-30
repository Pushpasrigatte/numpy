import numpy as np

a=np.arange(1,10)
print(a)

reshaped=a.reshape((3,3))
print(reshaped)

linear=reshaped.reshape(-1)
print(linear)