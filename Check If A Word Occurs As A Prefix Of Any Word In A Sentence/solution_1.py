class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        index = -1
        for i, word in enumerate(sentence.split()):
            if word.startswith(searchWord):
                index = i+1
                break
        return index