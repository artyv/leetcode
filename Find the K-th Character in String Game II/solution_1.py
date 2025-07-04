class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        n = math.ceil(math.log2(k))
        shift = 0
        for i in range(n, 0, -1):
            length = 2**i
            if k > length // 2:
                k -= length // 2
                if operations[i-1] == 1:
                    shift += 1

        res = chr(ord('a') + shift % 26)
        return res
