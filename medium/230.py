class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)

# heap - o(nlogn) runtime, o(n) space
import heapq

if not root:
    return 
heap = [root.val]
q = [root]
while q:
    cur_lvl = q
    q = []
    for i in cur_lvl:
        if i.left:
            q.append(i.left)
            heapq.heappush(heap, i.left.val)
        if i.right:
            q.append(i.right)
            heapq.heappush(heap, i.right.val)

return heapq.nsmallest(k, heap)[-1]

# recursive inorder - o(n) runtime, o(n) space
def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

ksmallest = inorder(root)[k-1]
return ksmallest

# iterative inorder 
if not root:
    return
inorder = []
stack = []
while True:
    while root:
        stack.append(root)
        root = root.left
    if not stack:
        return inorder
    node = stack.pop()
    inorder.append(node.val)
    k -= 1
    if k == 0:
        break
    root = node.right
return inorder[-1]