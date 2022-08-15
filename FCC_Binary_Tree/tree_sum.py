# Simple Node Class
class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Compute Total Sum of all values in the tree

def depth_first(root):
    if root is None:
        return 0
    stack = [root]  # Implementing Stack using Python List
    tree_sum = 0

    while len(stack) > 0:
        current = stack.pop()  # Popping top value off stack
        tree_sum += current.val
        if current.left is not None:
            stack.append(current.left)
        if current.right is not None:  # Right Side is added first since it is appended to stack last
            stack.append(current.right)

    return tree_sum


def depth_first_recursive(root):
    # Base Case
    if root is None:
        return 0

    # Recursive Case (Last Case is a.val + function(b) + function(c))
    return root.val + depth_first_recursive(root.left) + depth_first_recursive(root.right)


def breadth_first(root):
    if root is None:
        return 0
    queue = [root]
    tree_sum = 0

    while len(queue) > 0:
        current = queue.pop(0)
        tree_sum += current.val
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
    return tree_sum

# Constructing Nodes
a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(2)
f = Node(1)

# Connected each Node to represent a Binary Tree
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print(depth_first(a))
print(depth_first_recursive(a))
print(breadth_first(a))



