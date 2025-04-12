# Define the Node class for the tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Manual BFS function
def bfs(root):
    if root is None:
        return

    queue = []  # our manual FIFO queue
    queue.append(root)

    while len(queue) > 0:
        current = queue[0]    # get the front node
        queue = queue[1:]     # dequeue it (remove first element)
        
        print(current.value, end=' ')  # visit the node

        # enqueue left and right children if they exist
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)

def element_exists_bfs(root, target):
    if root is None:
        return False

    queue = [root]

    while len(queue) > 0:
        current = queue[0]
        queue = queue[1:]

        if current.value == target:
            print(f"Element {target} found in the tree.")
            return True

        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)

    return False



# Create the tree manually:
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

print("Manual BFS Traversal:")
bfs(root)
