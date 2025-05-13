# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        dmin = float('inf')
        prev = float('inf')

        def traverse(node):
            nonlocal dmin, prev
            if node is None:
                return

            if node.left is not None:
                traverse(node.left)
            
            dmin = min(dmin, abs(node.val - prev))
            prev = node.val
            
            if node.right is not None:
                traverse(node.right)
        
        traverse(root)
        return dmin
            

        