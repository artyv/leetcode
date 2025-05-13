# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1] * n for _ in range(m)]

        vector = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        vector_elem = 0
        i, j = 0, 0


        while head is not None:
            matrix[i][j] = head.val
            next_i = i + vector[vector_elem][0]
            next_j = j + vector[vector_elem][1]

            if min(next_i, next_j) < 0 or next_i >= m or next_j >= n or matrix[next_i][next_j] != -1:
                vector_elem += 1
                vector_elem %= 4
            i += vector[vector_elem][0]
            j += vector[vector_elem][1]

            head = head.next
        
        return matrix