class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        len_a = len(arr); len_q = len(queries)
        answer = [0] * len_q

        for i in range(1, len_a):
            arr[i] ^= arr[i-1]
        
        for i in range(len_q):
            if queries[i][0] == 0:
                answer[i] = arr[queries[i][1]]
            else:
                answer[i] = arr[queries[i][1]] ^ arr[queries[i][0]-1]
        
        return answer