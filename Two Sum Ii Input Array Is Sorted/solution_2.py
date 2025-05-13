class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}

        for i,x in enumerate(numbers):
            if x not in d:
                d[x] = [i]
            else:
                d[x].append(i)

        for key in d:
            if d.get(target-key, 0) != 0:
                if d[key] != d[target-key]:
                    return [d[key][0]+1, d[target-key][0]+1]
                else:
                    return [d[key][0]+1, d[key][1]+1]
