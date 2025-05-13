class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        counter = Counter(t)
        left = 0; chars_matched = 0
        output = ''; l_min = 10**10

        for right, c in enumerate(s):
            if c in counter:
                counter[c] -= 1
                chars_matched += counter[c] == 0
            while chars_matched == len(counter):
                if right - left + 1 < l_min:
                    l_min = right - left + 1
                    output = s[left:right+1]

                char_to_remove = s[left]
                left += 1
                if char_to_remove in counter:
                    chars_matched -= counter[char_to_remove] == 0
                    counter[char_to_remove] += 1
        
        return output
