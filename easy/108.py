class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
nums = [-10, -3, 0, 5, 9]

if not nums:
	return None

mid = len(nums) // 2
node = TreeNode(nums[mid])
node.left = self.sortedArrayToBST(nums[:mid])
node.right = self.sortedArrayToBST(nums[mid + 1:])
return node
