# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # iterative
        import collections

        if not root:
            return True
        stack = collections.deque([(root.left, root.right)])
        while stack:
            l, r = stack.pop()
            if not l and not r:
                continue
            elif not l or not r:
                return False
            if l.val != r.val:
                return False
            stack.append((l.left, r.right))
            stack.append((l.right, r.left))
        return True

        # recursive
        return self.dfs(root, root)


    def dfs(self, l, r):
        if not l and not r:
            return True
        elif not l or not r:
            return False

        return (l.val == r.val) and (self.dfs(l.left, r.right) and self.dfs(l.right, r.left))
