class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return len([x for x in details if x[-4:-2] > '60'])