class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        moves_sum = 0
        for i in range(len(seats)):
            moves_sum += abs(seats[i]-students[i])
        return moves_sum