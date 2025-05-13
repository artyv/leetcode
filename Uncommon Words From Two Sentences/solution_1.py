class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        lst1 = s1.split()
        lst2 = s2.split()

        counter = Counter(lst1) + Counter(lst2)

        return [word for word in counter if counter[word] == 1]