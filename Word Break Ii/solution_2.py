class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result = []
        #d = dict()
        #for word in wordDict:
        #    d[word] = True

        def backtrack(output, remaining):
            if not remaining:
                result.append(output.strip())
                return
            for i in range(len(remaining)-1, -1, -1):
                if remaining[i:] in wordDict:
                    backtrack(remaining[i:] + ' ' + output, remaining[:i])
        
        backtrack('', s)
        return result