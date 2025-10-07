import numpy as np

arr = np.array([1,2,3,4,5])

print("Original array: ", arr)

sorted_arr = np.sort(arr)

print("Sorted array: ", sorted_arr)

search_elt = 3

if search_elt in sorted_arr:
    print(f"{search_elt} is found at index:", np.where(arr==search_elt)[0][0])
else:
    print(f"{search_elt} is not found")

binary_index = np.searchsorted(sorted_arr, search_elt)

print(f"{search_elt} is found at index: {binary_index}")
