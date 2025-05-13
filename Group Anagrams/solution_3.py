class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for word in strs:
            key = ''.join(sorted(word))
            if key in d:
                d[key].append(word)
            else:
                d[key] = [word]
       
        return d.values()