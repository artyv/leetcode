class Solution:
    def numTeams(self, rating: List[int]) -> int:
        counter = 0
        l = len(rating)

        for i in range(1, l-1):
            counter += len([x for x in rating[:i] if x < rating[i]])*len([x for x in rating[i+1:] if x > rating[i]])
            counter += len([x for x in rating[:i] if x > rating[i]])*len([x for x in rating[i+1:] if x < rating[i]])
        
        return counter