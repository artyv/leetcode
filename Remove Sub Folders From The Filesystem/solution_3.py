class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key=len, reverse=True)
        res = []
        while folder:
            cur = folder.pop()
            res.append(cur)
            cur += '/'
            index = []
            for i in range(len(folder)):
                if cur in folder[i]:
                    index.append(i)
            print(index) 
            for ind in index[::-1]:
                folder.pop(ind)
        return res