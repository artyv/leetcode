# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        root.val = 0
        self.stack = [root]
        self.values = set()
        while self.stack:
            cur = self.stack.pop(0)
            if cur.left is not None:
                cur.left.val = cur.val * 2 + 1
                self.stack.append(cur.left)
            if cur.right is not None:
                cur.right.val = cur.val * 2 + 2
                self.stack.append(cur.right)
            
            self.values.add(cur.val)
        

    def find(self, target: int) -> bool:
        if target in self.values:
            return True
        else:
            return False


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)