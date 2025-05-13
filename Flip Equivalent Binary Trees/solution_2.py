# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and root2 or root1 and not root2:
            return False
        q1 = deque([root1]); q2 = deque([root2])
        while q1 or q2:
            if len(q1) != len(q2):
                return False

            n1 = len(q1);
            nodes1 = []; nodes2 = []
            for _ in range(n1):
                cur1 = q1.popleft()
                cur2 = q2.popleft()

                if not cur1 or not cur2:
                    continue

                if cur1 and cur1.left is not None:
                    q1.append(cur1.left)
                if cur1 and cur1.right is not None:
                    q1.append(cur1.right)
                
                if cur2 and cur2.left is not None:
                    q2.append(cur2.left)
                if cur2 and cur2.right is not None:
                    q2.append(cur2.right)

                nodes1.append(cur1.val)
                nodes2.append(cur2.val)
            if set(nodes1) != set(nodes2):
                return False
        return True
