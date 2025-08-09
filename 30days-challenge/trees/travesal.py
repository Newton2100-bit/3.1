# Tree Traversal - Three Basic Methods
# Tree structure:
#       1
#      / \
#     2   3
#    / \ / \
#   4  5 6  7

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Create the tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

def preorder_traversal(node, result=None):
    """Preorder: Root -> Left -> Right"""
    if result is None:
        result = []
    if node:
        result.append(node.val)        # Visit root first
        preorder_traversal(node.left, result)   # Then left subtree
        preorder_traversal(node.right, result)  # Then right subtree
    return result

def inorder_traversal(node, result=None):
    """Inorder: Left -> Root -> Right"""
    if result is None:
        result = []
    if node:
        inorder_traversal(node.left, result)    # Visit left subtree first
        result.append(node.val)                 # Then root
        inorder_traversal(node.right, result)   # Then right subtree
    return result

def postorder_traversal(node, result=None):
    """Postorder: Left -> Right -> Root"""
    if result is None:
        result = []
    if node:
        postorder_traversal(node.left, result)  # Visit left subtree first
        postorder_traversal(node.right, result) # Then right subtree
        result.append(node.val)                 # Finally root
    return result

# Demonstrate all three traversals
print("\033[4;2;36mTree Structure:\033[0m")
print("       1")
print("      / \\")
print("     2   3")
print("    / \\ / \\")
print("   4  5 6  7")
print()

print("\033[4;2;36m1. Preorder Traversal (Root -> Left -> Right):\033[0m")
preorder_result = preorder_traversal(root)
print(f"   Result: {preorder_result}")
print(f"   Order: {' -> '.join(map(str, preorder_result))}")
print()

print("\033[4;2;36m2. Inorder Traversal (Left -> Root -> Right):\033[0m")
inorder_result = inorder_traversal(root)
print(f"   Result: {inorder_result}")
print(f"   Order: {' -> '.join(map(str, inorder_result))}")
print()

print("\033[4;2;36m3. Postorder Traversal (Left -> Right -> Root):\033[0m")
postorder_result = postorder_traversal(root)
print(f"   Result: {postorder_result}")
print(f"   Order: {' -> '.join(map(str, postorder_result))}")
print()

print("\033[4;2;36mSummary:\033[0m")
print("- Preorder: Good for copying/serializing trees")
print("- Inorder: For BST, gives sorted order")
print("- Postorder: Good for deleting trees or calculating sizes")
