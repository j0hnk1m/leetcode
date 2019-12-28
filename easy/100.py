class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)
q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

# recursive dfs - o(n) runtime, o(d) space
def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if p and q:
        return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    elif not p and not q:
        return True
    return False

# iterative bfs - o(n) runtime, o(n) space
queue = [p, q]
while queue:
    cur_level = queue
    queue = []
    vals = [node.val if node else None for node in cur_level]
    if vals[:len(vals)//2] != vals[len(vals)//2:]:
        return False
    
    for i in cur_level:
        if i:
            queue.append(i.left)
            queue.append(i.right)
return True
        