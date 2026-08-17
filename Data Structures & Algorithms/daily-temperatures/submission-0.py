from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        sol = [0] * len(temperatures)
        stack = deque()

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                prevIndex = stack.pop()
                sol[prevIndex] = i-prevIndex
            stack.append(i)
        return sol
            