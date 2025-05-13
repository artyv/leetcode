class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        l = len(books)
        aux = [0] * (l+1)

        for i, x in enumerate(books, 1):
            cur_h = x[1]; cur_w = x[0]
            aux[i] = aux[i-1] + cur_h
            for j in range(i-1, 0, -1):
                cur_w += books[j-1][0]
                if cur_w > shelfWidth:
                    break
                cur_h = max(cur_h, books[j-1][1])
                aux[i] = min(aux[i], aux[j-1] + cur_h)
        return aux[l]