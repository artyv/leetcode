class Solution:
    def countSeniors(self, details: List[str]) -> int:
        counter = 0
        for x in details:
            if x[-4]+x[-3] > '60':
                counter += 1
        return counter