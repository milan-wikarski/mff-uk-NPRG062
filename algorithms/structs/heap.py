from math import log2, ceil
from random import randint


def sample(size, chooseFrom):
  res = []
  l = len(chooseFrom)

  for _ in range(size):
    res.append(chooseFrom[randint(0, l - 1)])

  return res


def swap(arr, a, b):
  temp = arr[a]
  arr[a] = arr[b]
  arr[b] = temp

  return arr


def ifelse(cond, t, f):
  if (cond):
    return t

  return f


def heapBubbleUp(heap, i):
  if (i > 1 and heap[i - 1] < heap[(i - 1) // 2]):
    swap(heap, i - 1, (i - 1) // 2)
    return heapBubbleUp(heap, i // 2)

  return heap


def heapBubbleDown(heap, i):
  # No children
  if (len(heap) < i * 2):
    return heap

  # Just left child
  if (len(heap) == i * 2 and heap[i * 2 - 1] < heap[i - 1]):
    swap(heap, i * 2 - 1, i - 1)
    return heap

  # Both children
  if (len(heap) > i * 2):
    if (heap[i * 2 - 1] < heap[i - 1] or heap[i * 2] < heap[i - 1]):
      side = ifelse(heap[i * 2 - 1] < heap[i * 2], 0, 1)
      swap(heap, i * 2 - 1 + side, i - 1)
      return heapBubbleDown(heap, i * 2 + side)


def heapBuild(arr):
  for i in range(len(arr) // 2 + 1, 0, -1):
    heapBubbleDown(arr, i)

  return arr


def heapPrint(heap):
  depth = ceil(log2(len(heap)))

  i = 0

  for d in range(depth):
    for _ in range(min(len(heap) - i, 2 ** d)):
      print(heap[i], end=" ")
      i += 1

    print("", end="\n")

  return heap


def heapMin(heap):
  return heap[0]


def heapInsert(heap, item):
  heap.append(item)
  return heapBubbleUp(heap, len(heap))


chooseFrom = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(10):
  arr = sample(5, chooseFrom)

  heap = heapBuild(arr)

  print(arr)
  print(heapMin(heap))

  for item in sample(5, chooseFrom):
    heapInsert(heap, item)

  print(heap)
  print(heapMin(heap))
