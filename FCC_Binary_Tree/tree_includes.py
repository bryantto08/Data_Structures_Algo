class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Tree Includes Solution using breadth first
def tree_includes_breadth(root, k):
    if root is None:
        return []
    queue = [root]

    while len(queue) > 0:
        current = queue.pop(0)
        # If Node Value equals k
        if current.val == k:
            return True

        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
    return False


# Tree Includes using Depth First Search Iteratively
def tree_includes_depth(root, k):
    if root is None:
        return False
    stack = [root]

    while len(stack) > 0:
        current = stack.pop()
        if current.val == k:
            return True
        if current.left is not None:
            stack.append(current.left)
        if current.right is not None:
            stack.append(current.right)
    return False

# Tree Includes Solution with Depth First Recursively
def tree_depth_recursive(root, k):
    # Base Case
    if root is None:
        return False
    if root.val == k:
        return True
    # Recursive Case
    return tree_depth_recursive(root.left, k) or tree_depth_recursive(root.right, k)


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

print(tree_includes_breadth(a, "g"))
print(tree_includes_depth(a, "f"))
print(tree_depth_recursive(a, "e"))
