# Find Max sum from root to leaf in Binary Tree

class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Depth First Search Recursively
def max_sum_tree(root):
    # Base Case
    if root is None:
        return 0

    # Recursive Case
    return max(max_sum_tree(root.left) + root.val, max_sum_tree(root.right) + root.val)


# Constructing Nodes
a = Node(5)
b = Node(11)
c = Node(3)
d = Node(4)
e = Node(2)
f = Node(1)

# Connected each Node to represent a Binary Tree
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print(max_sum_tree(a))


