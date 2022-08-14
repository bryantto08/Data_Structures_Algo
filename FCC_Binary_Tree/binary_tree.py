# Simple Node Class

class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

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

# Visualization
#        a
#       / \
#      b   c 
#     / \   \
#    d   e   f 

print(b.val)
print(a.left.val)


