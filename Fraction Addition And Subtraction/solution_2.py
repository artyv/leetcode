class Solution:
    def fractionAddition(self, expression: str) -> str:
        def find_gcd(a, b):
            if a == 0:
                return abs(b)
            return find_gcd(abs(b % a), abs(a))
        
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
        
        gcd = find_gcd(s, product)
        s //= gcd
        product //= gcd
        
        return f"{s}/{product}"
        
