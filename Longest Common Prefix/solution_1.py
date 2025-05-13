class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        elif len(strs) == 1:
            return strs[0]
        
        shortest_prefix = min(strs, key=len)
        while any(shortest_prefix not in words for words in strs):
            shortest_prefix = shortest_prefix[:-1]
        return shortest_prefix