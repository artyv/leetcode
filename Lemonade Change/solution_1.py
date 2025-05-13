class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count_5 = 0; count_10 = 0
        for x in bills:
            if x == 5:
                count_5 += 1
            elif x == 10:
                count_5 -= 1
                count_10 += 1
            else:
                if count_10:
                    count_10 -= 1
                    if count_5:
                        count_5 -= 1
                    else:
                        return False
                else:
                    count_5 -= 3
            if count_5 < 0:
                return False
        return True