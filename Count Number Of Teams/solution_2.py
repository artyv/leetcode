class Solution:
    def numTeams(self, rating: List[int]) -> int:
        counter = 0
        l = len(rating)

        for i in range(l-2):
            for j in range(i+1, l-1):
                if rating[i] > rating[j]:
                    counter += len([x for x in rating[j+1:] if x < rating[j]])
                elif rating[i] < rating[j]:
                    counter += len([x for x in rating[j+1:] if x > rating[j]])
        
        return counter