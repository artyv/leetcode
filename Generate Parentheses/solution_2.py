class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []

        def recursive_track(opening, closing, cur_str):
            if opening == 0 and closing == 0:
                output.append(cur_str)
            elif closing < opening or opening < 0:
                return
            recursive_track(opening-1, closing, cur_str+'(')
            recursive_track(opening, closing-1, cur_str+')')
        
        recursive_track(n, n, '')
        return output