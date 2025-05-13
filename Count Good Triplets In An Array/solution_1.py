class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 2)
    
    def update(self, index, value):
        index += 1  # BIT is 1-indexed
        while index < len(self.tree):
            self.tree[index] += value
            index += index & -index

    def query(self, index):
        # Sum from 0 to index
        index += 1
        res = 0
        while index:
            res += self.tree[index]
            index -= index & -index
        return res

class Solution:    
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        pos_in_nums2 = [0] * n
        for i, num in enumerate(nums2):
            pos_in_nums2[num] = i

        transformed = [pos_in_nums2[num] for num in nums1]

        # left[i] = number of elements before i that are less than transformed[i]
        left_tree = FenwickTree(n)
        left = [0] * n
        for i in range(n):
            left[i] = left_tree.query(transformed[i] - 1)
            left_tree.update(transformed[i], 1)

        # right[i] = number of elements after i that are greater than transformed[i]
        right_tree = FenwickTree(n)
        right = [0] * n
        for i in range(n - 1, -1, -1):
            right[i] = right_tree.query(n - 1) - right_tree.query(transformed[i])
            right_tree.update(transformed[i], 1)

        # total good triplets = sum of left[i] * right[i]
        return sum(l * r for l, r in zip(left, right))