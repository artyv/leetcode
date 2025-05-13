# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        sums = []; queue = deque([root])

        while queue:
            cur_sum = 0; n = len(queue)

            for _ in range(n):
                current = queue.popleft()
                cur_sum += current.val
            
                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)
            sums.append(cur_sum)

        if k > len(sums):
            return -1

        sums.sort(reverse=True)
        return sums[k-1]