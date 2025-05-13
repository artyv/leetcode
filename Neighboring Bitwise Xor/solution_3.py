class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        aux = [0]
        l = len(derived)
        for i in range(l):
            aux.append(derived[i] ^ aux[i])
        
        check = aux[0] == aux[-1]
        aux = [1]
        for i in range(l):
            aux.append(derived[i] ^ aux[i])
        
        return check or aux[0] == aux[-1]