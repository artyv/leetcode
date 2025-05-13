class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        aux = [(names[i], heights[i]) for i in range(len(names))]
        aux.sort(key=lambda x: x[1], reverse=True)
        return (x[0] for x in aux)