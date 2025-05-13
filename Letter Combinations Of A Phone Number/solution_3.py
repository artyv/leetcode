class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        l = len(digits)
        if l == 1:
            return list(d[digits[0]])
        
        output = []

        def recursion(comb, remaining):
            if len(remaining) == 0:
                output.append(comb)
                return
            for c in d[remaining[0]]:
                recursion(comb+c, remaining[1:])
        
        recursion('', digits)
        return output