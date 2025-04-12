# Define the Node class for the tree
class Node:
    def __init__(self, value):
        self.value = value      # value of the node
        self.left = None        # left child
        self.right = None       # right child


# 🔁 Manual DFS Preorder Traversal (Prints each node)
def dfs(root):
    if root is None:
        return  # base case: if the node is null, do nothing

    print(root.value, end=' ')  # 1. Visit the node

    dfs(root.left)             # 2. Traverse the left subtree
    dfs(root.right)            # 3. Traverse the right subtree


# 🔍 Manual DFS Search for a specific target value
def element_exists_dfs(root, target):
    if root is None:
        return False  # base case: if reached the end without finding

    if root.value == target:
        print(f"Element {target} found in the tree.")
        return True   # target found at this node

    # Recursively search in the left and right subtree
    return element_exists_dfs(root.left, target) or element_exists_dfs(root.right, target)


# 🌳 Manually Create the Binary Tree:
#         A
#       /   \
#      B     C
#     / \   / \
#    D   E F   G

root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.left = Node('F')
root.right.right = Node('G')


# ✅ DFS Traversal Output
print("Manual DFS Traversal (Preorder):")
dfs(root)  # Output: A B D E C F G

print("\n")  # newline for clarity

# ✅ DFS Search Test
element_exists_dfs(root, 'D')  # Output: Element D found in the tree.
element_exists_dfs(root, 'Z')  # Output: No output since 'Z' is not found
