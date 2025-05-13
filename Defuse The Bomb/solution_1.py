class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        len_code = len(code)
        if k == 0:
            return [0] * len_code
        code = code * 2
        aux = [-1] * len_code
        for i in range(len_code):
            if k > 0:
                aux[i] = sum(code[i+1:i+k+1])
            else:
                aux[i] = sum(code[len_code+i-abs(k):len_code+i])
        return aux