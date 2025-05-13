# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([(root, 0, -1)])
        while queue:
            n = len(queue)
            temp = []
            for _ in range(n): 
                cur, number, parent = queue.popleft()
        
                if cur.left is not None:
                    queue.append((cur.left, 2**number+1, number))
                if cur.right is not None:
                    queue.append((cur.right, 2**number+2, number))
                
                temp.append((cur, number, parent))
            values = [0] * n
            for i in range(n):
                values[i] = sum([x[0].val for x in temp if x[2] != temp[i][2]])
            for i in range(n):
                temp[i][0].val = values[i]
        return root