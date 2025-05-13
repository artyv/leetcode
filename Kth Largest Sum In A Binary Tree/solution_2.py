# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        nodes = []; queue = [(root, 0)]
        sums = []
        while len(queue):
            current, index = queue.pop(0)
            nodes.append((current.val, index))
            
            if current.left is not None:
                queue.append((current.left, index+1))
            if current.right is not None:
                queue.append((current.right, index+1))


        for x in nodes:
            if len(sums) > x[1]:
                sums[x[1]] += x[0]
            else:
                sums.append(x[0])
        sums.sort(reverse=True)
        return sums[k-1] if k <= len(sums) else -1