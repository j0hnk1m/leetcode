class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
s = TreeNode(3)
s.left = TreeNode(4)
s.right = TreeNode(5)
s.left.left = TreeNode(1)
s.left.right = TreeNode(2)
t = TreeNode(5)
t.left = TreeNode(1)
t.right = TreeNode(2)

# iterative bfs

