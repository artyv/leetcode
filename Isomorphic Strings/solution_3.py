class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        len_s, len_t = len(s), len(t)
        if len_s != len_t or len(set(s)) != len(set(t)):
            return False

        s_dict = {}; t_dict = {}

        for x in set(s):
            s_dict[x] = [i for i in range(len_s) if s[i] == x]

        for x in set(t):
            t_dict[x] = [i for i in range(len_t) if t[i] == x]


        return sorted(s_dict.values()) == sorted(t_dict.values())