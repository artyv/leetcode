class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        counter = prefix_sum = 0
        odd_count = 0
        even_count = 1

        for x in arr:
            prefix_sum += x
            if prefix_sum % 2 == 0:
                counter += odd_count
                even_count += 1
            else:
                counter += even_count
                odd_count += 1
            counter %= (10**9 + 7)

        return counter