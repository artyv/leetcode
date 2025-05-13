class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        letters = {'a', 'b', 'c'}
        generated_strings = []

        def generate(current_string):
            if len(current_string) == n:
                generated_strings.append(current_string)
                return
            
            for c in letters:
                if current_string and c != current_string[-1] or not current_string:
                    generate(current_string+c)
        
        generate('')
        
        if k > len(generated_strings):
            return ''
        else:
            return sorted(generated_strings)[k-1]