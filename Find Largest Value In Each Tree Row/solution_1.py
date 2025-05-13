# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return [] 
        
        queue = deque([root])
        result = []
        while queue:
            cur_row_max = float('-inf')
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)
                cur_row_max = max(cur_row_max, curr.val)
            result.append(cur_row_max)
        return result
            