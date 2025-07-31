import numpy as np

# an array with numbers from 10 to 50
arr = np.arange(10, 51)
print("Array from 10 to 50:", arr)

# find the maximum and minimum values
np.maximum_value = arr.max()
np.minimum_value = arr.min()
print("Maximum value:", np.maximum_value)
print("Minimum value:", np.minimum_value)

# multiply all elements by 3
# using the np.multiply function
arr_multiplied = np.multiply(arr, 3)
print("Array after multiplication by 3:", arr_multiplied)
