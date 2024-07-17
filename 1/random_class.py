#   tcellsx
import random
import numpy as np

arr=np.array([2,3,5,7,11,12,14,19,23,32])
Rint = random.randint(1,33)
while (Rint in arr):
    Rint = random.randint(1, 33)
print(Rint)
