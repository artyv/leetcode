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

        results = []
        def dfs(current_node):
            results.append(current_node.val)
            if current_node.left is not None:
                dfs(current_node.left)
            if current_node.right is not None:
                dfs(current_node.right)
        dfs(root)
        return floor(math.log2(len(results))) + 1
            