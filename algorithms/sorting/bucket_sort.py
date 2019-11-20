# Assume all keys in range {0, 1, ..., r-1}
def bucketSort(values, keys, r):
  res = []
  buckets = []

  for _ in range(r):
    buckets.append([])

  # Append value to the corresponding bucket
  for i in range(len(keys)):
    buckets[keys[i]].append(values[i])

  for bucket in buckets:
    for value in bucket:
      res.append(value)

  return res


# Assume item of values array in format [a1, a2, ..., ak]
# Assume that a1, a2, ..., ak in range {0, 1, ..., r-1}
def lexBucketSort(values, k, r):
  i = k - 1

  while (i >= 0):
    keys = []

    # Take i-th element as key
    for value in values:
      keys.append(value[i])

    values = bucketSort(values, keys, r)

    i -= 1

  return values
