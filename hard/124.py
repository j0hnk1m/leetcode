class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# recursive dfs 
res = float('-inf')

def maxPathSum(root: TreeNode) -> int:
    pathSum(root)
    return res
    
def pathSum(root):
    if not root:
        return 0
    global res
    left = pathSum(root.left) 
    right = pathSum(root.right)
    print(root.val)
    print(res)
    print()
    res = max(res, root.val + left + right)
    return max(root.val + max(left, right), 0)
