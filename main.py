import numpy as np
print(np.__version__)

list1 = [1, 2, 3, 4]

np_list2 = np.array(list1)
print(np_list2)

# double elements in an array
np_list2 = np_list2 + 5
print(np_list2)

# get number of dimensions
# print(arr.ndim); for example, np.array('A') is a 0-d array

lst= np.array([['A', 'B', 'C'], ['D', 'E', 'F']])
# starting from 2-d np arrays, elements in each list should be identical

print(lst.shape) # print the dimensions of the array

# lst[0][0] is chain indexing
# lst[0, 0] is indexing for numpy array


# -------------------------------------------------------------------------------
# slicing


array = np.array([[1, 2, 3, 4], 
                  [5, 6, 7, 8], 
                  [9, 10, 11, 12], 
                  [13, 14, 15, 16]])

print('\n\n---slicing practice starts here---\n\n')

# row
# array[start:end:step]
# [::2] pick every 2 rows, [::-1] pick every -1 rows (so basically reverse)

# column (such syntax is allowed in numpy only, not in standard python)
print(array[:, 0]) # select column 0
# array[:, -1] # select the last column

print(array[:, -1][::-1]) # print last column in reverse order
print(array[:, 0:2]) # print the first 2 columns
print(array[0:2, 0:3]) # print first 2 row * 3 columns


# -------------------------------------------------------------------------------
# scaler arithimetic

print('\n\n---scaler starts here---\n\n')
array = np.array([1, 2, 3])

print(array ** 3)

# -------------------------------------------------------------------------------
# vectorized math functions (apply a function to the entire array without a loop)

print('\n\n---vectors starts here---\n\n')
array = np.array([1.01, 2.5, 3.99])
print(np.ceil(array))

print('')

radii = np.array([1, 2, 3]) # a list of radius
print(np.pi * (radii ** 2)) # a list of area

# -------------------------------------------------------------------------------
# Element-wise arithmetic
print('\n\n---element-wise arithmetic starts here---\n\n')

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6]) # two arrays must have same shape here
print(arr1 + arr2)


# -------------------------------------------------------------------------------
# Comparison operators (filtering)
print('\n\n---comparison operators starts here---\n\n')

scores = np.array([91, 55, 100, 73, 82, 64])
print(scores == 100) # apply this boolean to every element in the array

scores[scores <= 60] = 0
scores[scores == 100] = 120 # manipuate arrays in a way similar to pandas series
print(scores)

# -------------------------------------------------------------------------------
# Broadcasting
# allows numpy to perform operations on arrays of different shapes
# by virtually expanding dimensions
# Requiring: each dimension should be either 1 or equal
print('\n\n---broadcasting starts here---\n\n')

arr1 = np.array([[1, 2, 3, 4]])
arr2 = np.array([[1], [2], [3], [4]])

print(arr1 * arr2)

# -------------------------------------------------------------------------------
# Aggregates
print('\n\n---aggregates starts here---\n\n')

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(np.sum(arr))
print(np.mean(arr))
print(np.std(arr)) # standard deviation
print(np.var(arr)) # variance
print(np.min(arr))
print(np.max(arr))
print(np.argmin(arr)) # return the index of the min element
print(np.argmax(arr)) # retuen the index of the max element
                      # only argmin and argmax exists

# sum the last column
print('\n', np.sum(arr[:, -1])) # 15

# sum each column
print('\n', np.sum(arr, axis = 0)) # axis = 0: sum all columns
# sum each row
print('\n', np.sum(arr, axis = 1)) # axis = 1: sum all rows


# -------------------------------------------------------------------------------
# Filtering
print('\n\n---filtering starts here---\n\n')
arr = [1, 3, 4, 9, 1, 8, 6, 10]
arr = np.array(arr)
print(arr[arr % 2 == 0])
print()

# using boolean indexing to filter flattens higher-d arrays
ages = np.array([[21, 17, 19, 20, 16, 30, 18, 65], 
                [35, 22, 15, 99, 18, 19, 20, 21]])
teenagers = ages[ages < 18]
print(teenagers)
print(ages[(ages >= 18) & (ages <= 65)]) # must use bitwise operators, and wrap in ()


# np.where() function preserves the shape of the array
adults = np.where(ages >= 18, ages, None) # (cond, array, filler
print(adults)
# Note that where is a lot slower than boolean indexing


# -------------------------------------------------------------------------------
# random numbers
print('\n\n---random numbers here---\n\n')

rng = np.random.default_rng() # random number generator = rng
print(rng.integers(1, 7), '\n') # random integer between [1, 7)
# or:
for i in range(10):
    print(rng.integers(low = 1, high = 3)) # {1, 2}

print(rng.integers(low = 1, high = 5, size = 3)) # an array of 3 random numbers

print(rng.integers(low = 1, high = 5, size = (3, 4))) 
# an multi-dimension array with given parameters of random numbers


rng_1 = np.random.default_rng(seed = 1) # can also set a seed for rng
print(rng_1.integers(0, 10, size = 10))

rng_2 = np.random.default_rng(seed = 1)
print(rng_2.integers(0, 10, size = 10)) # rng of same seed produce same output

print(np.random.uniform()) # a random floating number between 0, 1
print(np.random.uniform(low = -1, high = 1, size = 3))
# can set the seed using: np.random.seed(seed = 1)

# shuffle arrays
arr = np.array([1, 2, 3, 4, 'apple'])
rng = np.random.default_rng()
rng.shuffle(arr) # This is a pass by reference, so it changes the original array
for i in range(10):
    print(arr)
    rng.shuffle(arr)

# pick random elements from the array
rand_item1 = rng.choice(arr) # choice, not choose!!!
rand_item_list1 = rng.choice(arr, size = 3) # list of choice with duplicates
rand_item_list2 = rng.choice(arr, size = 3, replace = False) # without duplicates
rand_item_list3 = rng.choice(arr, size = (2, 3))
print('\n\n', rand_item1)
print(rand_item_list1)
print(rand_item_list2)
print(rand_item_list3)