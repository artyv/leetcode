class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7
        colors = [0, 1, 2]
        valid_cols = []

        # validity of column
        def is_valid(col):
            for i in range(1, len(col)):
                if col[i-1] == col[i]:
                    return False
            return True
        
        for col in itertools.product(colors, repeat=m):
            if is_valid(col):
                valid_cols.append(col)
        
        col_id = {col: id for id, col in enumerate(valid_cols)}
        compatible = defaultdict(list)

        for a in valid_cols:
            for b in valid_cols:
                if all(x != y for x,y in zip(a, b)):
                    compatible[col_id[a]].append(col_id[b])
        
        len_vc = len(valid_cols)
        dp = [1] * len_vc

        # n columns, first already have
        for _ in range(n-1):
            new_dp = [0] * len_vc
            for prev in range(len_vc):
                for cur in compatible[prev]:
                    new_dp[cur] = (new_dp[cur] + dp[prev]) % MOD
            dp = new_dp

        return sum(dp) % MOD

