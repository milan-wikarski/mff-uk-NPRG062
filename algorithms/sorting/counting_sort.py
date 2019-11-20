# Assumes all values in range {0, 1, ..., r-1}
def countingSort(values, r):
  res = []
  counts = [0] * (r + 1)

  # Count number of times element is in values
  for el in values:
    counts[el] += 1

  # Start with smallest element and append it counted number of times
  for i in range(r):
    for _ in range(counts[i]):
      res.append(i)

  return res
