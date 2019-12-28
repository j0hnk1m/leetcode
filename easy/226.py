class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

# recursive dfs - o(n) runtime, o(d) space
def invertTree(root: TreeNode) -> TreeNode:
    if not root:
        return
    tmp = root.left
    root.left = root.right
    root.right = tmp
    invertTree(root.left)
    invertTree(root.right)
    return root

# iterative bfs - o(n) runtime, o(n) space
if not root:
    return
q = [root]
while q:
    cur_level = q
    q = []
    for i in range(len(cur_level)):
        tmp = cur_level[i].left
        cur_level[i].left = cur_level[i].right
        cur_level[i].right = tmp
        
        if cur_level[i].left:
            q.append(cur_level[i].left)
        if cur_level[i].right:
            q.append(cur_level[i].right)
return root
