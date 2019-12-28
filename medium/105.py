class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

# recursive
def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    if inorder:
        root = TreeNode(preorder.pop(0))
        i = inorder.index(root.val)
        root.left = self.buildTree(preorder, inorder[0:i])
        root.right = self.buildTree(preorder, inorder[i+1:])
        return root
    return None
