# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def findNode(original, cloned, target):
            if not original:
                return None
            if original == target:
                return cloned
            return (
                findNode(original.left, cloned.left, target) 
                or findNode(original.right, cloned.right, target)
            )
        
        return findNode(original, cloned, target)
        
