from collections import deque
import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()

        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }

        for i in tokens:
            if i in ['+','-','*','/']:
                val2 = stack.pop()
                val1 = stack.pop()

                stack.append(int(ops[i](val1,val2)))
            else:
                stack.append(int(i))
        return stack.pop()