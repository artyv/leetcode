class Solution:
    def countAndSay(self, n: int) -> str:
        def cnt_digits(s):
            sout = ""
            lc = 1
            if len(s) > 1:
                for i in range(len(s)-1):
                    if s[i] == s[i+1]:
                        lc += 1
                    else:
                        sout += str(lc) + s[i]
                        lc = 1
                sout += str(lc) + s[-1]
            else:
                sout += str(s.count(s[0])) + s[0]
            return sout
        
        if n == 1:
            return '1'
        else:
            return cnt_digits(self.countAndSay(n-1))