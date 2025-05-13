class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def make_non_overlap(coord):
            left, right = coord[0]
            res = []

            for coord1, coord2 in coord:
                if coord1 >= right:
                    res.append((left, right))
                    left = coord1
                right = max(right, coord2)
            res.append((left, right))
            return res
        
        
        xs = []
        ys = []

        for x0,y0,x1,y1 in rectangles:
            xs.append((x0, x1))
            ys.append((y0, y1))
        
        xs.sort()
        ys.sort()

        not_overlap_x = make_non_overlap(xs)

        if len(not_overlap_x) >= 3:
            return True

        not_overlap_y = make_non_overlap(ys)

        if len(not_overlap_y) >= 3:
            return True

        return False