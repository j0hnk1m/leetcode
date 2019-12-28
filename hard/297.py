class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

def serialize(root):
    def tostr(node):
        if node:
            vals.append(str(node.val))
            tostr(node.left)
            tostr(node.right)
        else:
            vals.append('#')
    
    vals = []
    tostr(root)
    return ' '.join(vals)

def deserialize(data):
    def totree():
        val = next(vals)
        if val == '#':
            return None
        node = TreeNode(int(val))
        node.left = totree()
        node.right = totree()
        return node

    vals = iter(data.split())
    return totree()
