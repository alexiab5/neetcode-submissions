class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        result = [0] * n
        for i in range(n):
            while stack and temperatures[i] > stack[-1][0]:
                temp, index = stack.pop()
                result[index] = i - index
            stack.append((temperatures[i], i))
        return result