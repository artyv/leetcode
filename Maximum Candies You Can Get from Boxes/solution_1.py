class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        available_boxes = deque(initialBoxes)
        candies_collected = 0
        owned_keys, visited_boxes, waiting_boxes = set(), set(), set()

        while available_boxes:
            box = available_boxes.popleft()
            if box in visited_boxes: 
                continue
            
            if status[box] == 0 and box not in owned_keys:
                waiting_boxes.add(box)
                continue

            candies_collected += candies[box]
            for k in keys[box]:
                owned_keys.add(k)
                if k in waiting_boxes:
                    available_boxes.append(k)
                    waiting_boxes.remove(k)

            available_boxes.extend(containedBoxes[box])
            visited_boxes.add(box)
        
        return candies_collected
 
