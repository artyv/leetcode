class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i = 0; j = 0
        l1 = len(str1); l2 = len(str2)
        while i < l1 and j < l2:
            temp = 'a' if str1[i] == 'z' else chr(ord(str1[i])+1)
            if str1[i] == str2[j] or temp == str2[j]:
                j += 1
            i += 1
        return True if j == l2 else False
