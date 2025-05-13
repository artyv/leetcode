class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        parts = []
        while num:
            parts.append(num % 1000)
            num //= 1000
        d = {1: "One", 2: "Two", 3: "Three", 4: "Four",
            5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
            10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen",
            14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen",
            18: "Eighteen", 19: "Nineteen", 20: "Twenty", 30: "Thirty",
            40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy",
            80: "Eighty", 90: "Ninety", 100: "Hundred", 1000: "Thousand",
            1000_000: "Million", 1000_000_000: "Billion"
        }

        res = ''
        l = len(parts)
        def helper(n):
            output = []
            if n // 100:
                output.extend((n//100, 100))
            n %= 100
            if n in d:
                output.append(n)
            else:
                output.extend((n - n%10, n%10))
            return output

        while l:
            for el in helper(parts[-1]):
                res += d[el] + ' '
            if l > 1:
                res += d[10**(3*(l-1))] + ' '
            parts.pop()
            l -= 1
        return res.strip()