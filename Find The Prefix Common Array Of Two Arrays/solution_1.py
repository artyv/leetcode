class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        C = []
        a_set = set()
        b_set = set()
        for i in range(len(A)):
            a_set.add(A[i])
            b_set.add(B[i])
            C.append(len(a_set & b_set))
        return C