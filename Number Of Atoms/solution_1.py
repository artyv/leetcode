class Solution:
    def countOfAtoms(self, formula: str) -> str:
        d = dict()
        stack = [{}]
        l = len(formula); i = 0
        output = ''

        while i < l:
            if formula[i] == '(':
                stack.append({})
                i += 1
            elif formula[i] == ')':
                top = stack.pop()
                i += 1
                start = i
                while i < l and formula[i].isdigit():
                    i += 1
                multiplier = int(formula[start:i] or 1)
                for element, count in top.items():
                    stack[-1][element] = stack[-1].get(element, 0) + count * multiplier
            else:
                start = i
                i += 1
                while i < l and formula[i].islower():
                    i += 1
                element = formula[start:i]
                start = i
                while i < l and formula[i].isdigit():
                    i += 1
                count = int(formula[start:i] or 1)
                stack[-1][element] = stack[-1].get(element, 0) + count
    
        result = stack.pop()
        sorted_elements = sorted(result.keys())
        return ''.join(f"{element}{(result[element] if result[element] > 1 else '')}" for element in sorted_elements)