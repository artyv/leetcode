class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []

        while strs:
            cur_word = strs[0]
            temp = [x for x in strs if Counter(x) == Counter(cur_word)]
            answer.append(temp)
            filter_set = set(temp)
            strs = [x for x in strs if x not in filter_set]

        return answer
