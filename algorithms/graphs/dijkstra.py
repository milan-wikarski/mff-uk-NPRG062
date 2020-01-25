from math import inf


class Graph:
  def __init__(self, vertexes, edges, distances):
    self.vertexes = vertexes
    self.edges = edges
    self.distances = distances

  def has_edge(self, v, u):
    return u in self.edges[v]

  def get_distance(self, v, u):
    if (self.has_edge(v, u)):
      return self.distances[(v, u)]

    return None

  def shortest_path_from(self, v):
    opened = [False] * self.vertexes
    distances = [inf] * self.vertexes
    predecessors = [None] * self.vertexes

    opened[v] = True
    distances[v] = 0

    while (True):
      # Let v be the vertex with the minimal value of distances
      v = None
      for i in range(len(distances)):
        if (opened[i] and (v is None or distances[i] < distances[v])):
          v = i

      # Break when no vertex is opened
      if (v is None):
        break

      for w in self.edges[v]:
        if (distances[w] > distances[v] + self.get_distance(w, v)):
          distances[w] = distances[v] + self.get_distance(w, v)
          opened[w] = True
          predecessors[w] = v

      opened[v] = False

    return distances, predecessors


vertexes = 4
edges = [
    [1, 2],
    [0, 2],
    [0, 1, 3],
    [2]
]
distances = {
    (0, 1): 30,
    (1, 0): 30,

    (0, 2): 40,
    (2, 0): 40,

    (1, 2): 50,
    (2, 1): 50,

    (2, 3): 15,
    (3, 2): 15
}

graph = Graph(vertexes, edges, distances)

distances, predecessors = graph.shortest_path_from(0)

print(distances)
print(predecessors)
