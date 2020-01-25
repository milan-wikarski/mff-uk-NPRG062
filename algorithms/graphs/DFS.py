def if_none(value, t, f=None):
  if (value is None):
    return t

  if (f is None):
    return value

  return f


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


def DFS(vertexes, edges, start):
  def DFS_inner(v):
    nonlocal count, brackets
    opened[v] = True

    in_order[v] = count
    count += 1
    brackets += "({} ".format(v)

    for w in edges[v]:
      if (not opened[w]):
        DFS_inner(w)

    out_order[v] = count
    count += 1
    brackets += "){} ".format(v)

  brackets = ""
  opened = [False] * vertexes
  in_order = [None] * vertexes
  out_order = [None] * vertexes
  count = 1

  DFS_inner(start)

  return in_order, out_order, brackets


in_order, out_order, brackets = DFS(vertexes, edges, 0)

for v in range(vertexes):
  print("{0:<5}{1:<5}{2:<5}".format(
      v, if_none(in_order[v], "-"), if_none(out_order[v], "-")))

print(brackets)
