class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

if not root:
    return True
    
stack = [(root, float('-inf'), float('inf')), ] 
while stack:
    root, lower, upper = stack.pop()
    if root:
        val = root.val
        if val <= lower or val >= upper:
            return False
        stack.append((root.right, val, upper))
        stack.append((root.left, lower, val))
return True

