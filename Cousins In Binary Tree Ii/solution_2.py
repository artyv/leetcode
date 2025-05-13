# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([(root, root.val)])
        while queue:
            n = len(queue)
            level_sum = 0
            for x in queue:
                level_sum += x[0].val

            for _ in range(n): 
                cur, temp_sum = queue.popleft() # temp_sum is a sum of cur and its siblings values
                cur.val = level_sum - temp_sum
        
                childs_sum = 0
                if cur.left is not None:
                    childs_sum += cur.left.val
                if cur.right is not None:
                    childs_sum += cur.right.val

                if cur.left is not None:
                    queue.append((cur.left, childs_sum))
                if cur.right is not None:
                    queue.append((cur.right, childs_sum))

        return root