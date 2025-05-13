class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        counter = Counter(t)
        left = 0; right = len(t)-1
        output = ''

        while not (counter.items() <= Counter(s[left:right+1]).items()):
            print(counter, Counter(s[left:right+1]))
            if right == len(s)-1:
               break
            right += 1

        while counter.items() <= Counter(s[left+1:right+1]).items():
            left += 1
            output = s[left:right+1]

        output = s[left:right+1]
        left += 1; right += 1

        while right < len(s):
            while counter.items() <= Counter(s[left+1:right+1]).items():
                left += 1
                output = s[left:right+1]
            right += 1
            left += 1
        
        return output
