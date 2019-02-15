import numpy as np
from matplotlib import pyplot as plt

# Problem 1
nums = [1, 2, 3, 0, 0, 5, 10]
a = np.array(nums)
print('Array type:', type(a))
print('Array shape:', a.shape)

# Problem 2
a = np.arange(2, 11).reshape(3, 3)
print('3x3 Matrix:\n', a)

# Problem 3

# Method 1:
print('Reversed array using 1st method:')
a = [5, 4, 3, 2, 1, 100]
a_rev = a[::-1]
print(a_rev)

# Method 2
print('Reversed array using 2nd method:')
a = [5, 4, 3, 2, 1, 100]
for i in range(len(a) // 2):
    # in-place swaps
    a[i], a[-i - 1] = a[-i - 1], a[i]
print(a)

# Problem 4
a = np.array([1, 2, 3, 0])
print(np.append(a, 4))

# Problem 5
a = np.array([1, 2, 0, 0, 4, 0])
print(np.where(a != 0))

# Problem 6
null_vec = np.zeros(10)
print(null_vec)

# Problem 7
null_vec = np.zeros(10)
null_vec[4] = 1
print(null_vec)

# Problem 8
rand_vec = np.random.random(10)
rand_vec.sort()
print('Random vector of sorted values:\n', rand_vec)

# Problem 9
matrix = np.random.randint(100, size=40).reshape(5, 8)
print('Matrix:\n', matrix)
mean = matrix.mean(axis=1, keepdims=True)
print('Mean for each row:\n', mean)
# Subtract mean from each row using broadcasting
print(matrix - mean)

# Problem 10
data = [1, 2, 1, 3, 4, 5, 1, 3, 4, 1, 2, 3, 5, 4, 1, 2, 3, 4, 1, 3, 2]
bins = [0, 1, 2, 3, 4, 5, 6]
hist, bins = np.histogram(data, bins=bins)
print(hist, bins)

plt.hist(data, bins=bins)
plt.title("histogram")
plt.show()
