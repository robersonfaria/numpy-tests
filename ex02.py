import numpy as np

print(np.__version__)

arr = np.arange(10)
print(arr)

print(np.full((3, 3), True, dtype=bool))

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr[arr % 2 == 1])

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr[arr % 2 == 1] = -1
print(arr)


arr = np.arange(10)
out = np.where(arr % 2 == 1, -1, arr)
print('original', arr)
print('changed', out)

arr = np.arange(10)
print(arr.reshape(2, -1))