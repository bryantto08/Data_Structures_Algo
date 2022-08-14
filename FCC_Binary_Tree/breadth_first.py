# Simple Node Class
from queue import Queue


class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Breadth First Search Algorithm
def breadth_first(root):
    if root is None:
        return []
    # Creating Queue and Results array
    queue = [root]
    result = []

    # While there are elements in the queue
    while len(queue) > 0:
        current = queue.pop(0)
        result.append(current.val)
        # If node has children, add them to the queue
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
    return result


# Constructing Nodes
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

# Connected each Node to represent a Binary Tree
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print(breadth_first(a))


