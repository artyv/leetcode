class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(sum(int(num1[len(num1)-1-i])*10**i for i in range(len(num1))) * sum(int(num2[len(num2)-1-i])*10**i for i in range(len(num2))))