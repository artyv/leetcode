class Solution:
    def sumZero(self, n: int) -> List[int]:
        n_div = n // 2
        if n % 2 == 1:
            return [x for x in range(-n_div, n_div+1)]
        else:
            return [x for x in range(-n_div, n_div+1) if x != 0]
