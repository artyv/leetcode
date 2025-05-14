class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        def vector_matrix_mult(vec, mat, MODULO=10**9+7):
            res = [0] * A_L
            for j in range(A_L):
                for i in range(A_L):
                    res[j] = (res[j] + vec[i] * mat[i][j]) % MODULO
            return res
        
        def mat_mult(A, B, MODULO=10**9+7):
            size = len(A)
            res = [[0]*size for _ in range(size)]
            for i in range(size):
                for j in range(size):
                    for k in range(size):
                        res[i][j] = (res[i][j] + A[i][k]*B[k][j]) % MODULO
            return res

        def mat_pow(mat, power, MODULO=10**9+7):
            size = len(mat)
            res = [[int(i==j) for j in range(size)] for i in range(size)]
            while power:
                if power % 2 == 1:
                    res = mat_mult(res, mat, MODULO)
                mat = mat_mult(mat, mat, MODULO)
                power //= 2
            return res
        
        
        A_L = 26; MODULO = 10**9 + 7
        M = [[0]*A_L for _ in range(A_L)]
        for i in range(A_L):
            for step in range(nums[i]):
                j = (i + 1 + step) % A_L
                M[i][j] += 1
        
        counter = Counter(s)
        V = [counter.get(chr(ord('a') + i), 0) for i in range(A_L)]

        ans = vector_matrix_mult(V, mat_pow(M, t))

        return sum(ans) % MODULO
