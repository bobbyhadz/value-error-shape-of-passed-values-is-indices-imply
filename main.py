# ValueError: Shape of passed values is X, indices imply Y

import pandas as pd
import numpy as np

arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

print(arr.shape)  # 👉️ (3, 4)

df = pd.DataFrame(arr, columns=['A', 'B', 'C', 'D'])

#    A   B   C   D
# 0  1   2   3   4
# 1  5   6   7   8
# 2  9  10  11  12
print(df)
