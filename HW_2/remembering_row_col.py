import numpy as np

A = np.array([[1, 2],[3, 4], [5, 6]])

evals = np.array([1,6,4,8,3,2])
evecs = np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8]])

# edata = [x for _, x in sorted(zip(evals, evecs))]
# print(edata)

sorting_index = np.argsort(evals)
print(sorting_index)
evals = evals[sorting_index]
evecs = evecs[sorting_index]
print(evecs)
print(evals)