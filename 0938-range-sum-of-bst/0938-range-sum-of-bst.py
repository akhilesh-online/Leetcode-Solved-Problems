# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sum = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def findSum(root):
            if root:
                findSum(root.left)
                if low <= root.val <= high:
                    self.sum += root.val
                findSum(root.right)
        findSum(root)
        return self.sum