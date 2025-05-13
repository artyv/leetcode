class Solution:
    def fractionAddition(self, expression: str) -> str:
        j = 0
        for i, c in enumerate(expression):
            if c == '-':
                expression = expression[:i+j] + '+' + expression[i+j:]
                j += 1
        
        numerator = []; denominator = []
        product = 1
        for frac in expression.split('+'):
            if frac:
                fr = frac.split('/')
                numerator.append(int(fr[0]))
                product *= int(fr[1])
                denominator.append(int(fr[1]))
        s = 0
        for i in range(len(numerator)):
            s += numerator[i] * (product//denominator[i])
        
        for x in range(2, product//2+1):
            while s % x == 0 and product % x == 0:
                s //= x
                product //= x
        
        return f"{s}/{product}"
        
