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

  @property
  def empty(self):
    return self.first is None


vertexes = 10

edges = [
    [1, 3, 9],
    [2, 3],
    [],
    [4],
    [],
    [3],
    [0, 3, 7],
    [],
    [6],
    [6]
]

# print("EDGES")
# for i, neighbors in enumerate(edges):
#   print("{}: {}".format(i, ", ".join(list(map(str, neighbors)))))


def BFS(vertexes, edges, start):
  discovered = [False] * vertexes
  distances = [None] * vertexes
  parents = [None] * vertexes
  layers = []

  distances[start] = 0
  discovered[start] = True
  layers.append([start])

  queue = Queue()
  queue.enqueue(start)

  while (not queue.empty):
    v = queue.dequeue()
    for w in edges[v]:
      if (not discovered[w]):
        discovered[w] = True
        distances[w] = distances[v] + 1
        parents[w] = v

        if (len(layers) == distances[v] + 1):
          layers.append([])
        layers[distances[v] + 1].append(w)

        queue.enqueue(w)

  return discovered, distances, parents, layers


def BFS_components(vertexes, edges):
  components = [None] * vertexes

  for start in range(vertexes):
    if (components[start] is None):
      components[start] = start
      queue = Queue()
      queue.enqueue(start)

      while (not queue.empty):
        v = queue.dequeue()
        for w in edges[v]:
          if (components[w] is None):
            components[w] = start
            queue.enqueue(w)

  return components


discovered, distances, parents, layers = BFS(vertexes, edges, 0)
components = BFS_components(vertexes, edges)

print("COMPONENTS")
for i, component in enumerate(components):
  print("{}: {}".format(i, component))

# print("DISTANCES")
# for i, distance in enumerate(distances):
#   print("{}: {}".format(i, distance))

# print("LAYERS")
# for i, layer in enumerate(layers):
#   print("{}: {}".format(i, ", ".join(list(map(str, layer)))))

# print("PARENTS")
# for i, parent in enumerate(parents):
#   print("{}: {}".format(i, parent))

# Print("Path from start to 7")
# path = []
# v = 7
# while (v is not None):
#   path.append(v)
#   v = parents[v]

# print(" --> ".join(list(map(str, path[::-1]))))
