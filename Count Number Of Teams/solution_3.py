class Solution:
    def numTeams(self, rating: List[int]) -> int:
        counter = 0
        l = len(rating)

        for i in range(1, l-1):
            x_before_less = 0; x_before_more = 0
            x_after_less = 0; x_after_more = 0
            for j in range(i):
                if rating[j] < rating[i]:
                    x_before_less += 1
                elif rating[j] > rating[i]:
                    x_before_more += 1
            
            for j in range(i+1, l):
                if rating[j] < rating[i]:
                    x_after_less += 1
                elif rating[j] > rating[i]:
                    x_after_more += 1
            
            counter += (x_before_less * x_after_more) + (x_before_more * x_after_less)
        
        return counter