# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
    
        def helper(current_node, value, output):
            if current_node.val == value:
                return True
            elif current_node.left is not None and helper(current_node.left, value, output):
                output += 'L'
            elif current_node.right is not None and helper(current_node.right, value, output):
                output += 'R'
            return output
        
        start = []; dest = []
        helper(root, startValue, start)
        helper(root, destValue, dest)
        while start and dest and start[-1] == dest[-1]:
            start.pop()
            dest.pop()
        return "".join("U" * len(start)) + "".join(reversed(dest))