class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        return abs(sum(seats)-sum(students))