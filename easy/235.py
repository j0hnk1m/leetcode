class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
p = TreeNode(2)
q = TreeNode(8)

# recursive - o(n) runtime, o(n) space
def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if p.val < root.val and q.val < root.val:
        return lowestCommonAncestor(root.left, p, q)
    elif p.val > root.val and q.val > root.val:
        return lowestCommonAncestor(root.right, p, q)
    return root

# iterative - o(n) runtime, o(1) space
while root:
    if p.val < root.val and q.val < root.val:
        node = node.left
    elif p.val > root.val and q.val > root.val:
        node = node.right
    return root
