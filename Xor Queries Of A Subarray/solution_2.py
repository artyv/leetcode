class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        len_a = len(arr); len_q = len(queries)
        aux = [0] * len_a; aux[0] = arr[0]
        answer = [0] * len_q

        for i in range(1, len_a):
            aux[i] = aux[i-1] ^ arr[i]
        
        for i in range(len_q):
            if queries[i][0] == 0:
                answer[i] = aux[queries[i][1]]
            else:
                answer[i] = aux[queries[i][1]] ^ aux[queries[i][0]-1]
        
        return answer