# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        q = [root]
        tree = [[root.val]]
        while q:
            node_lst = q
            level = [i for i in node_lst]
            neighbors = []
            for i in level:
                if i.left:
                    neighbors.append(i.left)
                if i.right:
                    neighbors.append(i.right)
            if neighbors:
                tree.append([k.val for k in neighbors])
            q = neighbors
        
        return tree
