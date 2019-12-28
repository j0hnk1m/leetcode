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
t = TreeNode(4)
t.left = TreeNode(1)
t.right = TreeNode(2)

# recursive
def equals(a, b):
    if not a and not b:
        return True
    elif not a or not b:
        return False
    return a.val == b.val and equals(a.left, b.left) and equals(a.right, b.right)

def isSubtree(s: TreeNode, t: TreeNode) -> bool:
    if not s and not t:
        return True
    elif not s or not t:
        return False
    return equals(s, t) or isSubtree(s.left, t) or isSubtree(s.right, t)
