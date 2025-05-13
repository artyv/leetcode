# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.counter = 0

        def dfs(current_node):
            if not current_node:
                return []
            if current_node.left is None and current_node.right is None:
                return [1]
            
            left = dfs(current_node.left)
            right = dfs(current_node.right)

            for l in left:
                for r in right:
                    if l + r <= distance:
                        self.counter += 1
            results = [i+1 for i in left+right if i+1 < distance]
            return results
        
        dfs(root)
        return self.counter
