# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def BFS(root):
            current = root
            queue = [current]; results = []
            while len(queue) > 0:
                current = queue.pop(0)
                results.append(current and current.val)
                if current is not None:
                    queue.append(current.left)
                    queue.append(current.right)   
                
            return results
        
        return BFS(p) == BFS(q)