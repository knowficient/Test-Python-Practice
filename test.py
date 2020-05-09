import numpy as np
import matplotlib.pyplot as plt

check = np.zeros((10, 10))
check[::2, 1::2] = 1 #row(st=N:sp=N:step=2)  column (st=1:sp=N:step=2)
print(check)
check[1::2, ::2] = 1 #row(st=1:sp=N:step=2)  column (st=N:sp=N:step=2)
print(check)
plt.matshow(check, cmap='gray')
plt.show()