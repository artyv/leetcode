class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        return sorted(list(set([int(''.join(x)) for x in permutations(map(str, digits), 3) if int(''.join(x)) % 2 == 0 and x[0] != '0'])))