from heap import Heap
from random import randint
from time import time


def is_sorted(arr):
  for i in range(len(arr) - 1):
    if (arr[i] > arr[i + 1]):
      return False

  return True


class SpeedTest:
  def __init__(self, n, low=0, high=999):
    self.n = n

    self.low = low
    self.high = high

    self.results = []

  def run(self, times=1):
    for _ in range(times):
      items_after = []

      start = time()

      heap = Heap()

      for i in range(n):
        heap.insert(randint(self.low, self.high))

      while (not heap.empty):
        items_after.append(heap.extract())

      self.results.append(time() - start)

      if (not is_sorted(items_after)):
        raise Exception("Items not sorted")

    return self

  @property
  def result(self):
    return sum(self.results) / len(self.results)


STEP = 500
ITERATIONS = 200
N_TESTS = 100
START = 0

for i in range(ITERATIONS):
  f = open("speed-test.csv", "a")
  n = (i + 1) * STEP + START
  test = SpeedTest(n).run(N_TESTS)

  text = "\n{0},{1}".format(n, test.result)

  f.write(text)
  print(text, end="")

  f.close()
