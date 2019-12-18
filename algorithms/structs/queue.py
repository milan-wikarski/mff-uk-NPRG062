class QueueItem:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


class Queue:
  def __init__(self, items=[]):
    self.first = None
    self.last = None

    for item in items:
      self.enqueue(item)

  def __str__(self):
    item = self.first
    res = []

    while (item is not None):
      res.append(item.value)
      item = item.next

    return "[" + " <-- ".join(list(map(str, res))) + "]"

  def enqueue(self, value):
    item = QueueItem(value)

    if (self.first is None):
      self.first = item
      self.last = item
      return self

    self.last.next = item
    self.last = item

  def dequeue(self):
    if (self.first is None):
      raise Exception("No items in queue")

    value = self.first.value

    self.first = self.first.next

    if (self.first is None):
      self.last = None

    return value
