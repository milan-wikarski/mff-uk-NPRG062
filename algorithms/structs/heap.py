from math import ceil, log2


class Array(object):

  def __init__(self, items: list) -> None:
    self.items = items

  def __repr__(self) -> str:
    return '{}({})'.format(self.__class__.__name__, self.items)

  def __len__(self) -> int:
    return len(self.items)

  def __contains__(self, item: any) -> bool:
    return item in self.items

  def __getitem__(self, key: int) -> any:
    return self.items[key - 1]

  def __setitem__(self, key: int, value: any) -> None:
    self.items[key - 1] = value

  def __delitem__(self, key: int) -> None:
    del self.items[key - 1]

  def append(self, item) -> int:
    self.items.append(item)
    return len(self.items)

  def pop(self, index=None):
    if (index is None):
      index = len(self)

    item = self[index]
    self.items.pop(index - 1)

    return item

  @staticmethod
  def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


class Heap(object):

  def __init__(self, items=[]) -> None:
    self.items = Array(items)

    self.count = {
        "bubble_up": 0,
        "bubble_down": 0
    }

    for i in range(self.length // 2 + 1):
      self._bubble_down(i + 1)

  def __str__(self):
    return str(self.items)

  def _swap(self, a, b):
    Array.swap(self.items, a, b)
    return self

  def _bubble_up(self, i):
    self.count["bubble_up"] += 1

    if (i > 1 and self.items[i // 2] > self.items[i]):
      return self._swap(i // 2, i)._bubble_up(i // 2)

    return self

  def _bubble_down(self, i):
    self.count["bubble_down"] += 1

    # Just one child
    if (i * 2 == self.length):
      if (self.items[i * 2] < self.items[i]):
        return self._swap(i * 2, i)

    # Two children
    elif (i * 2 < self.length):
      smaller = i * 2

      if (self.items[i * 2 + 1] < self.items[i * 2]):
        smaller += 1

      if (self.items[smaller] < self.items[i]):
        return self._swap(smaller, i)._bubble_down(smaller)

    # No children
    return self

  def insert(self, item):
    self.items.append(item)
    return self._bubble_up(self.length)

  def extract(self):
    min = self.min

    self._swap(1, self.length)
    self.items.pop()

    self._bubble_down(1)

    return min

  @property
  def length(self):
    return len(self.items)

  @property
  def empty(self):
    return bool(self.length == 0)

  @property
  def depth(self):
    return ceil(log2(self.length))

  @property
  def min(self):
    return self.items[1]
