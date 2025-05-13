# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def dfs(current_node, count):
            if current_node is None:
                return count
            return max(dfs(current_node.left, count+1), dfs(current_node.right, count+1))
        
        return dfs(root, 0)
            