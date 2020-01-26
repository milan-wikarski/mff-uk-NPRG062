class Node:
  def __init__(self, value=None, left=None, right=None):
    self.left = left
    self.right = right
    self.value = value
    self.size = None  # Size of the subtree with root in this node


class Tree:
  def __init__(self, root: Node):
    self.root = root

  def _post_order_default_callback(self, node):
    print(node.value, end=' ')

  def post_order(self, callback=None):
    if (callback is None):
      callback = self._post_order_default_callback

    def post_order_inner(node):
      nonlocal callback
      if (node is not None):
        post_order_inner(node.left)
        post_order_inner(node.right)
        callback(node)

    post_order_inner(self.root)

  def is_perfectly_balanced(self):
    def explore(node):
      if (node is not None):
        explore(node.left)
        explore(node.right)

        right = 0 if node.right is None else node.right.size
        left = 0 if node.left is None else node.left.size

        if (abs(right - left) > 1):
          return False

        node.size = 1 + right + left

    res = explore(self.root)

    if (res is None):
      res = True

    return res


T1 = Tree(
    Node(0,
         Node(1,
              Node(4,
                   Node(90),
                   Node(25)
                   ),
              Node(9,
                   Node(15),
                   Node(5)
                   )
              ),
         Node(2,
              Node(3,
                   Node(8)
                   ),
              Node(20)
              )
         )
)

T2 = Tree(
    Node(0,
         Node(1),
         Node(2,
              Node(3)
              )
         )
)

T1.post_order()
print('| {}'.format(T1.is_perfectly_balanced()))

T2.post_order()
print('| {}'.format(T2.is_perfectly_balanced()))
