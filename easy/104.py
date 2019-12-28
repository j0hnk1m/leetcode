class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# recursive dfs - o(n) runtime
if not root:
    return 0
return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

# iterative bfs - o(n) runtime, o(n) space
if not root:
    return 0

q = [root]
depth = 0
while q:
    depth += 1
    next_level = []
    for i in q:
        if i.left:
            next_level.append(i.left)
        if i.right:
            next_level.append(i.right)
    q = next_level
return depth
