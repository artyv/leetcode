class Solution:
    def maximumSwap(self, num: int) -> int:
        def comp(s1, s2):
            counter = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    counter += 1
            if counter <= 2:
                return True
            return False

        s = str(num)
        p = permutations(sorted(str(num), reverse=True))
        for x in p:
            if comp(''.join(x), s):
                return int(''.join(x))
