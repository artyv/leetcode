class Solution:
    def minSwaps(self, s: str) -> int:
        balance = 0; counter = 0
        l = len(s); j = l-1
        s = list(s)

        for i in range(len(s)):
            if s[i] == '[':
                balance += 1
            else:
                if balance > 0:
                    balance -= 1
                else:
                    while j > i:
                        if s[j] == '[':
                            s[i], s[j] = s[j], s[i]
                            counter += 1
                            break
                        j -= 1
                    balance += 1
        return counter