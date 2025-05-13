class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        letters = 'abc'
        ans = ''
        counter = 0

        def generate(current_string):
            nonlocal ans, counter
            if len(current_string) == n:
                counter += 1
                if counter == k:
                    ans = current_string
                return
            
            for c in letters:
                if not current_string or c != current_string[-1]:
                    generate(current_string+c)
                    if ans:
                        return
        
        generate('')
        return ans