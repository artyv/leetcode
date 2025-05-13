class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        len_a = len(arr)
        aux = [0] * (len_a + 1)

        for i in range(len_a):
            aux[i+1] = aux[i] ^ arr[i]
        
        answer = [aux[right+1] ^ aux[left] for left,right in queries]
        
        return answer