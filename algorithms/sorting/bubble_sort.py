from autoload import *


def bubbleSort(arr):
  n = len(arr)
  stop = False

  # Repeat until no swaps in this cycle
  while (not stop):
    stop = True

    for i in range(1, n):
      # Swap two closest elements if they are in incorrect order
      if (arr[i - 1] > arr[i]):
        stop = False
        swap(arr, i - 1, i)

  return arr
