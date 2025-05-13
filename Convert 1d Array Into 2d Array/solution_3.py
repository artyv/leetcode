class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        return ((original[i + j*n] for i in range(n)) for j in range(m))