class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        counter = Counter(hand)
        for x in sorted(counter):
            freq = counter[x]
            if freq != 0:
                for i in range(groupSize):
                    if freq > counter.get(x+i, 0):
                        return False
                    counter[x+i] -= freq
        return True