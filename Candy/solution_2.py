class Solution:
    def candy(self, ratings: List[int]) -> int:
        len_list = len(ratings)
        candies = [1] * len_list

        for i in range(len_list - 1):
            if ratings[i] < ratings[i+1]:
                candies[i+1] = candies[i] + 1

        for i in range(len_list - 1, 0, -1):
            if ratings[i-1] > ratings[i]:
                candies[i-1] = candies[i] + 1
        
        return sum(candies)