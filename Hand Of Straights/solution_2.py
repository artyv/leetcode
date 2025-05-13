class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        times = len(hand) // groupSize
        for _ in range(times):
            m = min(hand)
            hand.remove(m)
            group_end = m + groupSize
            m += 1
            while m < group_end:
                if m not in hand:
                    return False
                hand.remove(m)
                m += 1
        return True