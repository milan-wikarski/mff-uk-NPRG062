from autoload import *


def selectSort(arr):
  n = len(arr)

  # Iterate over all elements
  for i in range(n):
    # Assume first element is smallest
    minIndex = i
    # Sorted part of the array is of length i
    # + 1 because if minIndex assumption
    for j in range(i + 1, n):
      if (arr[j] < arr[minIndex]):
        minIndex = j

    # Swap i-th element with minimal element in unsorted part of the array
    swap(arr, i, minIndex)

  return arr
