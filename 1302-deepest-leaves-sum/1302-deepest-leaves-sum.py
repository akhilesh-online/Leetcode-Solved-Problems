# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        traversed_nodes_list = [root]
        while traversed_nodes_list:
            parent_nodes_list, traversed_nodes_list = traversed_nodes_list, [child for each_node in traversed_nodes_list for child in [each_node.left, each_node.right] if child]
        return sum(each_node.val for each_node in parent_nodes_list)