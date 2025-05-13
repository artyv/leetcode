class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        res = []
        a = set(dictionary)
        
        for word in sentence.split():
            for i in range(len(word)):
                if word[:i+1] in a:
                    res.append(word[:i+1])
                    break
            else:
                res.append(word)
    
        return ' '.join(res)