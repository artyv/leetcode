class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def dfs(chain, lcur, lmin):
            if lcur == lmin:
                return chain
            for i in range(len(chain[-1])):
                stemp = chain[-1][:i] + chain[-1][i+1:]
                print(stemp)
                if stemp in words:
                    chain.append(stemp)
                    return dfs(chain, lcur-1, lmin)
        
        words.sort(key=len, reverse=True)
        chain = [words[0]]
        dfs(chain, len(words[0]), len(words[-1]))
        return len(chain)
                