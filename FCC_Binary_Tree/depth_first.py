# Creating a Depth-First Search algorithm

# Simple Node Class
class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Depth First Search Algorithm (Iteratively)
def depth_first(root):
    # If root is Null
    if root == None:
        return []
    
    # First onto stack is root
    stack = [root]
    result = []

    while len(stack) > 0:
        current = stack.pop()

        result.append(current.val)
        # Depth First Search Prioritizing Left Side because Right Side is being Pushed first
        if current.right != None:
            stack.append(current.right)
        if current.left != None:
            stack.append(current.left)
    
    return result
        
# Depth First Search Algorithm (Recursively)
def depth_first_recursive(root):
    # Base Case
    if root == None:
        return []
    
    # Recursive Case
    left_value = depth_first_recursive(root.left) # [b, d, e]
    right_value = depth_first_recursive(root.right) # [c, f]
    return [root.val] + left_value + right_value




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

# print(depth_first(a))
print(depth_first_recursive(a))