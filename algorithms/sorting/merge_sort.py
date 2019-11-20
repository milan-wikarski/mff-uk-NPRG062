# Merge two sorted arrays a and b
def merge(a, b):
  res = []

  while (len(a) > 0 or len(b) > 0):
    if (len(a) == 0):
      res.append(b.pop(0))
    elif (len(b) == 0):
      res.append(a.pop(0))
    elif (a[0] < b[0]):
      res.append(a.pop(0))
    else:
      res.append(b.pop(0))

  return res


def mergeSort(arr):
  chunks = []

  # Start by placing all elements into separate chunk
  for i in range(len(arr)):
    chunks.append([arr[i]])

  # Repeat until left with just one chunk
  while (len(chunks) > 1):
    newChunks = []

    # Merge all neighbors
    for i in range(len(chunks) // 2):
      newChunks.append(merge(chunks[i * 2], chunks[i * 2 + 1]))

    # If odd number of chunks append the last one that has no other chunk to merge with
    if (len(chunks) % 2 == 1):
      newChunks.append(chunks[len(chunks) - 1])

    chunks = newChunks

  return chunks[0]
