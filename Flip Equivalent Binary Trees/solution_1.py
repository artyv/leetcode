# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False

        q1 = deque([(root1, -1)]) 
        q2 = deque([(root2, -1)])
        
        while q1 and q2:
            if len(q1) != len(q2):
                return False

            n1 = len(q1);
            nodes1 = []; nodes2 = []
            
            for _ in range(n1):
                cur1, parent1 = q1.popleft()
                cur2, parent2 = q2.popleft()

                if not cur1 and not cur2:
                    continue
                if not cur1 or not cur2:
                    return False

                if cur1.left is not None:
                    q1.append((cur1.left, cur1.val))
                if cur1.right is not None:
                    q1.append((cur1.right, cur1.val))
                
                if cur2 and cur2.left is not None:
                    q2.append((cur2.left, cur2.val))
                if cur2 and cur2.right is not None:
                    q2.append((cur2.right, cur2.val))

                nodes1.append((cur1.val, parent1))
                nodes2.append((cur2.val, parent2))
            
            if set(nodes1) != set(nodes2):
                return False
        
        return True
