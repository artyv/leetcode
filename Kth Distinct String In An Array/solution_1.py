class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        res = ''
        counter = Counter(arr)
        for s in arr:
            if counter[s] == 1:
                k -= 1
                if k == 0:
                    res = s
                    break
        return res
