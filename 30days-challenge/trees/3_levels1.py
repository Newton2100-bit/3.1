class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def create_sample_tree():
    """
    Creates a 4-level binary tree:
               1
            /     \
           2       3
         /  \     /  \
        4    5   6    7
       /\   /\  /\   /\
      8  9 10 11 12 13 14 15
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    # Level 4 nodes
    root.left.left.left = TreeNode(8)
    root.left.left.right = TreeNode(9)
    root.left.right.left = TreeNode(10)
    root.left.right.right = TreeNode(11)
    root.right.left.left = TreeNode(12)
    root.right.left.right = TreeNode(13)
    root.right.right.left = TreeNode(14)
    root.right.right.right = TreeNode(15)

    return root

# Algorithm 1: Inorder Traversal (Left -> Root -> Right)
def inorder_traversal(root):
    """
    Inorder: Left -> Root -> Right
    For BST, this gives nodes in sorted order
    """
    result = []

    def inorder_helper(node):
        if node:
            inorder_helper(node.left)   # Visit left subtree
            result.append(node.val)     # Visit root
            inorder_helper(node.right)  # Visit right subtree

    inorder_helper(root)
    return result

# Algorithm 2: Preorder Traversal (Root -> Left -> Right)
def preorder_traversal(root):
    """
    Preorder: Root -> Left -> Right
    Good for copying tree structure or creating prefix expressions
    """
    result = []

    def preorder_helper(node):
        if node:
            result.append(node.val)     # Visit root
            preorder_helper(node.left)  # Visit left subtree
            preorder_helper(node.right) # Visit right subtree

    preorder_helper(root)
    return result

# Algorithm 3: Postorder Traversal (Left -> Right -> Root)
def postorder_traversal(root):
    """
    Postorder: Left -> Right -> Root
    Good for deleting tree or calculating directory sizes
    """
    result = []

    def postorder_helper(node):
        if node:
            postorder_helper(node.left)  # Visit left subtree
            postorder_helper(node.right) # Visit right subtree
            result.append(node.val)      # Visit root

    postorder_helper(root)
    return result

# Iterative implementations using stacks
def iterative_inorder(root):
    """
    Iterative inorder using stack
    """
    result = []
    stack = []
    current = root

    while stack or current:
        # Go to leftmost node
        while current:
            stack.append(current)
            current = current.left

        # Current is None, pop from stack
        current = stack.pop()
        result.append(current.val)

        # Visit right subtree
        current = current.right

    return result

def iterative_preorder(root):
    """
    Iterative preorder using stack
    """
    if not root:
        return []

    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node.val)

        # Push right first, then left (so left is processed first)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result

def iterative_postorder(root):
    """
    Iterative postorder using two stacks
    """
    if not root:
        return []

    stack1 = [root]
    stack2 = []
    result = []

    # First stack for traversal, second for result order
    while stack1:
        node = stack1.pop()
        stack2.append(node)

        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)

    # Pop from second stack to get postorder
    while stack2:
        result.append(stack2.pop().val)

    return result

# Step-by-step demonstration function
def demonstrate_traversals_step_by_step(root):
    """
    Shows how each traversal visits nodes step by step
    """
    print("=== STEP-BY-STEP TRAVERSAL DEMONSTRATION ===")
    print()

    # Inorder step-by-step
    print("INORDER (Left → Root → Right):")
    steps = []
    def inorder_demo(node, depth=0):
        if node:
            print(f"{'  ' * depth}Going left from {node.val}")
            inorder_demo(node.left, depth + 1)
            steps.append(node.val)
            print(f"{'  ' * depth}Visiting {node.val}")
            inorder_demo(node.right, depth + 1)

    inorder_demo(root)
    print(f"Final order: {steps}")
    print()

    # Preorder step-by-step
    print("PREORDER (Root → Left → Right):")
    steps = []
    def preorder_demo(node, depth=0):
        if node:
            steps.append(node.val)
            print(f"{'  ' * depth}Visiting {node.val}")
            preorder_demo(node.left, depth + 1)
            preorder_demo(node.right, depth + 1)

    preorder_demo(root)
    print(f"Final order: {steps}")
    print()

    # Postorder step-by-step  
    print("POSTORDER (Left → Right → Root):")
    steps = []
    def postorder_demo(node, depth=0):
        if node:
            postorder_demo(node.left, depth + 1)
            postorder_demo(node.right, depth + 1)
            steps.append(node.val)
            print(f"{'  ' * depth}Visiting {node.val}")

    postorder_demo(root)
    print(f"Final order: {steps}")
    print()

# Main demonstration
if __name__ == "__main__":
    # Create the sample tree
    tree = create_sample_tree()

    print("4-LEVEL BINARY TREE STRUCTURE:")
    print("        1")
    print("     /     \\")
    print("    2       3")
    print("   / \\     / \\")
    print("  4   5   6   7")
    print(" /\\  /\\  /\\  /\\")
    print("8 9 10 11 12 13 14 15")
    print()

    print("=== THE THREE DFS TRAVERSAL ALGORITHMS ===")
    print()

    # Algorithm 1: Inorder
    print("1. INORDER TRAVERSAL (Left → Root → Right):")
    print(f"   Recursive:  {inorder_traversal(tree)}")
    print(f"   Iterative:  {iterative_inorder(tree)}")
    print("   Use cases: BST sorting, expression evaluation")
    print()

    # Algorithm 2: Preorder  
    print("2. PREORDER TRAVERSAL (Root → Left → Right):")
    print(f"   Recursive:  {preorder_traversal(tree)}")
    print(f"   Iterative:  {iterative_preorder(tree)}")
    print("   Use cases: Tree copying, prefix expressions, file system listing")
    print()

    # Algorithm 3: Postorder
    print("3. POSTORDER TRAVERSAL (Left → Right → Root):")
    print(f"   Recursive:  {postorder_traversal(tree)}")
    print(f"   Iterative:  {iterative_postorder(tree)}")
    print("   Use cases: Tree deletion, directory size calculation, postfix expressions")
    print()

    # Comparison table
    print("=== TRAVERSAL COMPARISON ===")
    inorder_result = inorder_traversal(tree)
    preorder_result = preorder_traversal(tree)
    postorder_result = postorder_traversal(tree)

    print("┌───────────┬─────────────────────────────────────────────────────────┐")
    print("│ Traversal │ Result                                                  │")
    print("├───────────┼─────────────────────────────────────────────────────────┤")
    print(f"│ Inorder   │ {str(inorder_result):<55} │")
    print(f"│ Preorder  │ {str(preorder_result):<55} │")
    print(f"│ Postorder │ {str(postorder_result):<55} │")
    print("└───────────┴─────────────────────────────────────────────────────────┘")
    print()

    # Optional: Uncomment to see step-by-step demonstration
    # demonstrate_traversals_step_by_step(tree)
