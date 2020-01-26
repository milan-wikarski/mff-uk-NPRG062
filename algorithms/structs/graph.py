from math import inf
from counter import Counter
from queue import Queue


def implode(arr, sep=', '):
  return sep.join(list(map(str, arr)))


def if_none(value, t, f=None):
  if (value is None):
    return t

  if (f is None):
    return value

  return f


class Graph:
  # @prop {set.<any>} vertices - list of vertices
  # @prop {list.<set.<int>>} edges - i-th element is a list of vertices connected by an edge with i-th vertex
  def __init__(self, vertices: set, edges: dict):
    self.vertices = vertices
    self.edges = edges

  def __str__(self):
    vertices = implode(self.vertices)

    edges = ''
    for i, key in enumerate(self.edges):
      edges += f'  {key}: {implode(self.edges[key])}'
      if (i + 1 < len(self.edges)):
        edges += '\n'

    return(f'VERTICES\n  {vertices}\nEDGES  \n{edges}')

  def add_vertex(self, v):
    self.vertices.add(v)
    return self

  def add_edge(self, v, u):
    raise NotImplementedError('Mehtod `add_edge` is not implemented')

  def remove_edge(self, v, u):
    raise NotImplementedError('Mehtod `remove_edge` is not implemented')

  def remove_vertex(self, v):
    raise NotImplementedError('Mehtod `remove_vertex` is not implemented')

  def has_edge(self, v, u):
    return u in self.edges[v]

  def BFS(self, v0):
    discovered = dict()
    distances = dict()
    parents = dict()
    layers = []

    for v in self.vertices:
      discovered[v] = False
      distances[v] = None
      parents[v] = None

    distances[v0] = 0
    discovered[v0] = True
    layers.append([v0])

    queue = Queue()
    queue.enqueue(v0)

    while (not queue.empty):
      v = queue.dequeue()
      for w in self.edges[v]:
        if (not discovered[w]):
          discovered[w] = True
          distances[w] = distances[v] + 1
          parents[w] = v

          if (len(layers) == distances[v] + 1):
            layers.append([])
          layers[distances[v] + 1].append(w)

          queue.enqueue(w)

    return distances, parents, layers

  def DFS(self, v0):
    counter = Counter(0)
    brackets = ''
    opened = dict()
    in_order = dict()
    out_order = dict()

    for v in self.vertices:
      opened[v] = False
      in_order[v] = None
      out_order[v] = None

    def DFS_inner(v):
      nonlocal counter, brackets, opened, in_order, out_order
      opened[v] = True

      in_order[v] = counter.next()
      brackets += '({} '.format(v)

      for w in self.edges[v]:
        if (not opened[w]):
          DFS_inner(w)

      out_order[v] = counter.next()
      brackets += '){} '.format(v)

    DFS_inner(v0)

    return in_order, out_order, brackets


class UndirectedGraph(Graph):
  def add_edge(self, v, u):
    self.edges[v].add(u)
    self.edges[u].add(v)
    return self

  def remove_edge(self, v, u):
    self.edges[v].remove(u)
    self.edges[u].remove(v)
    return self

  def remove_vertex(self, v):
    for w in self.edges[v]:
      self.edges[w].remove(v)

    del self.edges[v]
    self.vertices.remove(v)
    return self

  def components(self):
    counter = Counter(0)
    components = dict()
    for v in self.vertices:
      components[v] = None

    for v0 in self.vertices:
      if (components[v0] is None):
        components[v0] = counter.next()
        queue = Queue()
        queue.enqueue(v0)

        while (not queue.empty):
          v = queue.dequeue()
          for w in self.edges[v]:
            if (components[w] is None):
              components[w] = counter.current
              queue.enqueue(w)

    return components


class WeightedGraph(Graph):
  def __init__(self, vertices: list, edges: dict, weights: dict):
    super().__init__(vertices, edges)
    self.weights = weights

  def __str__(self):
    res = super().__str__() + '\nWEIGHTS\n'
    for i, (v, u) in enumerate(self.weights):
      weight = self.weights[(v, u)]
      res += '  {} <--> {}: {}'.format(v, u, weight)
      if (i + 1 < len(self.weights)):
        res += '\n'

    return res

  def add_edge(self, v, u, weight):
    self.weights[(v, u)] = weight
    self.weights[(u, v)] = weight
    return super().add_edge(v, u)

  def remove_edge(self, v, u):
    del self.weights[(v, u)]
    del self.weights[(u, v)]
    return super().remove_edge(v, u)

  def remove_vertex(self, v):
    for u, w in self.weights:
      if (u == v or w == v):
        del self.weights[(u, w)]
    return super().remove_vertex(v)

  # Dijkstra's algorithm
  def shortest_path_from(self, v0):
    distances = dict()
    opened = dict()
    parents = dict()
    for v in self.vertices:
      distances[v] = inf
      opened[v] = False
      parents[v] = None

    opened[v0] = True
    distances[v0] = 0

    while (True):
      v = None
      for w in distances:
        if (opened[w] and (v is None or distances[w] < distances[v])):
          v = w

      if (v is None):
        break

      for w in self.edges[v]:
        if (distances[w] > distances[v] + self.weights[(v, w)]):
          distances[w] = distances[v] + self.weights[(v, w)]
          opened[w] = True
          parents[w] = v

      opened[v] = False

    return distances, parents


class DirectedGraph(Graph):
  def add_edge(self, v, u):
    self.edges[v].add(u)
    return self

  def remove_edge(self, v, u):
    self.edges[v].remove(u)
    return self

  def remove_vertex(self, v):
    for w in self.vertices:
      if (v in self.edges[w]):
        self.edges[w].remove(v)

    del self.edges[v]
    self.vertices.remove(v)
    return self


class WeightedUndirectedGraph(WeightedGraph, UndirectedGraph):
  pass


class WeightedDirectedGraph(WeightedGraph, DirectedGraph):
  pass


vertices = {'a', 'b', 'c', 'd'}
edges = {
    'a': {'b', 'c'},
    'b': {'a', 'c'},
    'c': {'a', 'b', 'd'},
    'd': {'c'}
}
weights = {
    ('a', 'b'): 30,
    ('b', 'a'): 30,

    ('a', 'c'): 40,
    ('c', 'a'): 40,

    ('b', 'c'): 50,
    ('c', 'b'): 50,

    ('c', 'd'): 15,
    ('d', 'c'): 15
}

G = WeightedUndirectedGraph(vertices, edges, weights)

print(G, end='\n\n')

# SECTION DFS
# in_order, out_order, brackets = G.DFS('a')

# print('{0:<5}|{1:<5}|{2:<5}'.format('v', 'in', 'out'))
# print('-' * 17)
# for key in G.vertices:
#   print('{0:<5}|{1:<5}|{2:<5}'.format(
#       key, if_none(in_order[key], '-'), if_none(out_order[key], '-')))

# print(brackets)
# !SECTION


# SECTION BFS
# distances, parents, layers = G.BFS('a')

# print('DISTANCES')
# for key in distances:
#   print('  {}: {}'.format(key, distances[key]))

# print('PARENTS')
# for key in parents:
#   print('  {}: {}'.format(key, parents[key]))

# print('LAYERS')
# for i, layer in enumerate(layers):
#   print('  {}: {}'.format(i, ', '.join(list(map(str, layer)))))
# !SECTION


# SECTION Components
# components = G.components()

# print('COMPONENTS')
# for key in components:
#   print('  {}: {}'.format(key, components[key]))
# !SECTION


# SECTION Dijkstra
# distances, parents = G.shortest_path_from('a')
# print('DISTANCES')
# for key in distances:
#   print('  {}: {}'.format(key, distances[key]))

# print('PARENTS')
# for key in parents:
#   print('  {}: {}'.format(key, parents[key]))
# !SECTION
