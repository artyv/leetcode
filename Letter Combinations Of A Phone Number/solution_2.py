class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        l = len(digits)
        if l == 1:
            return list(d[digits[0]])
        
        output = list(d[digits[0]])

        for i in range(1, l):
            for _ in range(len(output)):
                s1 = output.pop(0)
                output.extend(s1+s2 for s2 in d[digits[i]])
        
        return output