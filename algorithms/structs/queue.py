class QueueItem:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


class Queue:
  def __init__(self, items=[]):
    self.first = None

    for item in items:
      self.enqueue(item)

  def __str__(self):
    item = self.first
    res = []

    while (item is not None):
      res.append(item.value)
      item = item.next

    return "[" + " <-- ".join(list(map(str, res))) + "]"

  @property
  def empty(self):
    return self.first is None

  @property
  def last(self):
    if (self.empty):
      return None

    current = self.first
    while (current.next is not None):
      current = current.next

    return current

  @property
  def length(self):
    count = 0

    current = self.first
    while (current is not None):
      count += 1
      current = current.next

    return count

  def _default_cmp(self, a, b):
    return a < b

  def enqueue(self, value):
    item = QueueItem(value)

    if (self.empty):
      self.first = item
    else:
      self.last.next = item

    return self

  def dequeue(self):
    if (self.empty):
      raise Exception("No items in queue")

    value = self.first.value
    self.first = self.first.next

    return value

  def get_min(self, comp=None):
    if (self.empty):
      return None

    if (comp is None):
      comp = self._default_cmp

    res = self.first.value
    current = self.first.next
    while (current is not None):
      if (comp(current.value, res)):
        res = current.value
      current = current.next

    return res

  def get_max(self, comp=None):
    if (self.empty):
      return None

    if (comp is None):
      comp = self._default_cmp

    res = self.first.value
    current = self.first.next
    while (current is not None):
      if (comp(res, current.value)):
        res = current.value
      current = current.next

    return res

  # Append another queue to the end of this queue
  def append(self, queue):
    self.last.next = queue.first
    return self

  @staticmethod
  # Input:    two queues sorted in descending order
  # Output:   one queue with all unique values from the two queues
  #             sorted in descending orders
  def merge(a, b):
    if (a.empty):
      return b

    if (b.empty):
      return a

    if (b.first.value < a.first.value):
      a, b = b, a

    ca = a.first
    while (b.first is not None):
      if (ca.value == b.first.value):
        b.first = b.first.next
      elif (ca.next is None or ca.next.value > b.first.value):
        a_temp = ca.next
        b_temp = b.first
        b.first = b.first.next
        ca.next = b_temp
        b_temp.next = a_temp
      else:
        ca = ca.next

    return a


a = Queue([9, 25, 1])
b = Queue([4, 16, 36])

print(a.append(b).get_max())
