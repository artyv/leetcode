class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        x_freq = [(k, v) for k, v in counter.items()]
        x_freq.sort(key=lambda x:x[0], reverse=True)
        x_freq.sort(key=lambda x: x[1])

        output = []
        for k, v in x_freq:
            output.extend([k]*v)

        return output
        


