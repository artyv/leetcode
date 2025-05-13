class Solution:
    def nearestPalindromic(self, n: str) -> str:
        def palindrome_from_half(first_half, is_even):
            res = first_half
            if not is_even:
                first_half //= 10
            while first_half:
                res = res * 10 + first_half % 10
                first_half //= 10
            return res
        
        l = len(n); is_even = l % 2 == 0
        dmin = float('inf'); res = 0
        half_index = (l//2 - 1) if l % 2 == 0 else (l // 2)
        first_half = int(n[:half_index+1])
        possibilities = []
        
        # in total 5 possible options
        possibilities.append(10 **(l - 1) - 1)
        possibilities.append(10**l + 1)

        possibilities.append(palindrome_from_half(first_half, is_even))
        possibilities.append(palindrome_from_half(first_half-1, is_even))
        possibilities.append(palindrome_from_half(first_half+1, is_even))

        for x in possibilities:
            if x == int(n):
                continue
            if abs(x - int(n)) < dmin:
                dmin = abs(x - int(n))
                res = x
            elif abs(x - int(n)) == dmin:
                res = min(x, res)
        return str(res)