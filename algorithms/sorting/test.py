from select_sort import selectSort
from bubble_sort import bubbleSort
from merge_sort import mergeSort
from counting_sort import countingSort
from bucket_sort import bucketSort, lexBucketSort


def simpleTest(name, fun, arr):
  print(name + ":")
  print("   Unsorted ", end="")
  print(arr)
  print("     Sorted ", end="")
  print(fun(arr), end="\n\n\n")


def countingSortTest():
  r = 5
  values = [1, 2, 3, 1, 2, 4, 0, 3, 2, 0, 4, 1, 1]
  print("Counting Sort:")
  print("   Unsorted ", end="")
  print(values)
  print("     Sorted ", end="")
  print(countingSort(values, r), end="\n\n\n")


def bucketSortTest():
  r = 5
  values = [11, 23, 45, 1, 7, 9, 45, 90, 12]
  keys = [1, 2, 4, 1, 2, 0, 0, 3, 2]
  print("Bucket Sort:")
  print("       Keys ", end="")
  print(keys)
  print("   Unsorted ", end="")
  print(values)
  print("     Sorted ", end="")
  print(bucketSort(values, keys, r), end="\n\n\n")


def lexBucketSortTest():
  r = 10
  k = 3
  values = [[1, 7, 3], [7, 5, 3], [2, 7, 3], [
      3, 5, 1], [1, 7, 1], [1, 7, 2], [0, 6, 9]]
  print("Lex Bucket Sort:")
  print("   Unsorted ", end="")
  print(values)
  print("     Sorted ", end="")
  print(lexBucketSort(values, k, r), end="\n\n\n")


smallArr = [4, 2, 1, 9, 7, 5]

print("SIMPLE TESTS\n")
simpleTest("Select Sort", selectSort, smallArr[:])
simpleTest("Bubble Sort", bubbleSort, smallArr[:])
simpleTest("Merge Sort", mergeSort, smallArr[:])

countingSortTest()

bucketSortTest()

lexBucketSortTest()
