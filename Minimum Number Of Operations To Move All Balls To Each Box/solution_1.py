class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0] * len(boxes)
        for current_box in range(len(boxes)):
            if boxes[current_box] == "1":
                for new_position in range(len(boxes)):
                    ans[new_position] += abs(new_position - current_box)
        return ans