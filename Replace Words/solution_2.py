class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        res = ''
        for word in sentence.split():
            for i in range(len(word)):
                if word[:i+1] in dictionary:
                    res += word[:i+1]
                    break
            else:
                res += word
            res += ' '
        return res.strip()