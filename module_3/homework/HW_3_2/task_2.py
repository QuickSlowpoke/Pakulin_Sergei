import numpy as np
from random import randint

n = 5
m = [[randint(0, 100) for i in range(n)] for j in range(n)]
print(m)

maximum = np.max(m)
print(maximum)