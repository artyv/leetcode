class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        res = []
        l = len(expression)

        if l == 0:
            return res
        elif l == 1 or l == 2:
            return [int(expression)]


        for i, c in enumerate(expression):
            if c.isdigit():
                continue

            # Split the expression into left and right parts
            left_results = self.diffWaysToCompute(expression[:i])
            right_results = self.diffWaysToCompute(expression[i+1:])

            # Combine results from left and right parts
            for left_value in left_results:
                for right_value in right_results:
                    if c == "+":
                        res.append(left_value + right_value)
                    elif c == "-":
                        res.append(left_value - right_value)
                    elif c == "*":
                        res.append(left_value * right_value)

        return res