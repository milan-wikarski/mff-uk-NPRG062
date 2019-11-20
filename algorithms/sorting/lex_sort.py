def lexSort(strings):
  lengths = []
  maxLen = 0

  # Calculate lengths and find the max length
  for string in strings:
    l = len(string)
    lengths.append(l)
    maxLen = max(maxLen, l)

  lenBuckets = []

  for _ in range(maxLen + 1):
    lenBuckets.append([])

  # Put each string into correct bucket based on length
  for i in range(len(strings)):
    lenBuckets[len(strings[i])].append(strings[i])

  # final = []

  # i = maxLen

  # while (i >= 0):
  #   lexBuckets = []

  #   for string in lenBuckets[i]:
  #     lexBuckets[string[i - 1]]

  #   i -= 1

  print(lenBuckets)


lexSort(["lorem", "ipsum", "dolor", "sit", "amet"])
