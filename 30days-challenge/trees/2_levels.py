class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def create_sample_tree():
    """
    Creates a 3-level binary tree:
            1
          /   \
         2     3
        / \   / \
       4   5 6   7
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    return root

# Algorithm 1: Depth-First Search (DFS) - Inorder Traversal
def inorder_traversal(root):
    """
    Inorder: Left -> Root -> Right
    """
    result = []
    
    def inorder_helper(node):
        if node:
            inorder_helper(node.left)   # Visit left subtree
            result.append(node.val)     # Visit root
            inorder_helper(node.right)  # Visit right subtree
    
    inorder_helper(root)
    return result

# Algorithm 2: Depth-First Search (DFS) - Preorder Traversal
def preorder_traversal(root):
    """
    Preorder: Root -> Left -> Right
    """
    result = []
    
    def preorder_helper(node):
        if node:
            result.append(node.val)     # Visit root
            preorder_helper(node.left)  # Visit left subtree
            preorder_helper(node.right) # Visit right subtree
    
    preorder_helper(root)
    return result

# Algorithm 3: Breadth-First Search (BFS) - Level Order Traversal
def level_order_traversal(root):
    """
    BFS: Visit nodes level by level from left to right
    """
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        node = queue.pop(0)  # Dequeue from front
        result.append(node.val)
        
        # Add children to queue
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result

# Bonus: DFS Postorder Traversal
def postorder_traversal(root):
    """
    Postorder: Left -> Right -> Root
    """
    result = []
    
    def postorder_helper(node):
        if node:
            postorder_helper(node.left)  # Visit left subtree
            postorder_helper(node.right) # Visit right subtree
            result.append(node.val)      # Visit root
    
    postorder_helper(root)
    return result

# Iterative versions using stacks/queues
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

# Demonstration
if __name__ == "__main__":
    # Create the sample tree
    tree = create_sample_tree()
    
    print("Tree Structure:")
    print("      1")
    print("    /   \\")
    print("   2     3")
    print("  / \\   / \\")
    print(" 4   5 6   7")
    print()
    
    # Run all traversal algorithms
    print("=== TRAVERSAL ALGORITHMS ===")
    print()
    
    print("1. DFS - Inorder (Left-Root-Right):")
    print(f"   Recursive: {inorder_traversal(tree)}")
    print(f"   Iterative: {iterative_inorder(tree)}")
    print()
    
    print("2. DFS - Preorder (Root-Left-Right):")
    print(f"   Recursive: {preorder_traversal(tree)}")
    print(f"   Iterative: {iterative_preorder(tree)}")
    print()
    
    print("3. BFS - Level Order (Breadth-First):")
    print(f"   Result: {level_order_traversal(tree)}")
    print()
    
    print("Bonus - DFS Postorder (Left-Right-Root):")
    print(f"   Result: {postorder_traversal(tree)}")
    print()
    
    # Show level-by-level breakdown for BFS
    print("=== BFS LEVEL-BY-LEVEL BREAKDOWN ===")
    root = tree
    if root:
        queue = [root]
        level = 1
        
        while queue and level <= 3:
            level_size = len(queue)
            level_nodes = []
            
            for _ in range(level_size):
                node = queue.pop(0)
                level_nodes.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            print(f"Level {level}: {level_nodes}")
            level += 1
