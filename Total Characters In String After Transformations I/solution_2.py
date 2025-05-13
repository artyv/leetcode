class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        counter = Counter(s)
        MODULO = 10**9 + 7

        for _ in range(t):
            new_d = defaultdict(int)
            for c,v in counter.items():
                if c == 'z':
                    new_d['a'] += v
                    new_d['b'] += v
                else:
                   new_d[chr(ord(c)+1)] += v 
            
            counter = new_d
        
        return sum(counter.values()) % MODULO