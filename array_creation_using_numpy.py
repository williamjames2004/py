import numpy as np

arr1 = np.array([1,2,3,4,5])

print("1D array: ", arr1)

arr2 = np.array([[1,2,3,4],[5,6,7,8]])

print("2D array: ", arr2)

print("Array addition: ", arr1+5)

print("Array Multiplication: ", arr1*2)

print("First 3 elements: ", arr1[:3])

newarr = np.arange(1,10).reshape(3,3)
print("Reshaped array\n: ", newarr)
