class Solution:
    def countAndSay(self, n: int) -> str:
        output = ['0'] * (n+1)
        output[1] = '1'
        for i in range(2, n+1):
            sc = ''
            lc = 1
            temp = output[i-1]
            if len(temp) == 1:
                output[i] = '11'
                continue
            for j in range(len(temp)-1):
                if temp[j] == temp[j+1]:
                    lc += 1
                else:
                    sc += str(lc) + temp[j]
                    lc = 1
            sc += str(lc) + temp[-1]
            output[i] = sc
        
        return output[n]
