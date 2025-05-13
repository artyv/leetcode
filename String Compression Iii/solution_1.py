class Solution:
    def compressedString(self, word: str) -> str:
        counter = Counter(word)
        freq = sorted([[k, v] for k,v in counter.items()], key=lambda x: x[1], reverse=True)
        comp = ''
        while freq:
            if freq[0][1] > 9:
                freq[0][1] -= 9
                comp += '9' + freq[0][0]
            else:
                comp += str(freq[0][1]) + freq[0][0]
                freq.pop(0)
        return comp
