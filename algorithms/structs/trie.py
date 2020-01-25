class Node:
  def __init__(self, children, key, value=None):
    self.key = key
    self.value = value

    self.children = [None] * children


class Trie:
  def __init__(self, alphabet="abcdefghijklmnopqrstuvwxyz"):
    self.alphabet_size = len(alphabet)
    self.alphabet = dict()

    n = 0
    for char in list(alphabet):
      self.alphabet[char] = n
      n += 1

    self.root = Node(self.alphabet_size, "")

  def set(self, key, value):
    node = self.root

    for char in list(key):
      index = self.alphabet[char]

      if (node.children[index] is None):
        node.children[index] = Node(self.alphabet_size, char)

      node = node.children[index]

    node.value = value

  def get(self, key):
    node = self.root

    for char in list(key):
      index = self.alphabet[char]

      if (node.children[index] is None):
        return None

      node = node.children[index]

    return node.value
