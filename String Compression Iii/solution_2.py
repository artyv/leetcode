class Solution:
    def compressedString(self, word: str) -> str:
        comp = ''
        i = 0; l = len(word)
        while i < l:
            counter = 1
            while i+counter < l and counter < 9 and word[i] == word[i+counter]:
                counter += 1
            comp += str(counter) + word[i]
            i += counter
        return comp
