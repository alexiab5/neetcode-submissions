class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p in '([{':
                stack.append(p)
            else:
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if (last == '(' and p != ')') or last == '[' and p != ']' or last == '{' and p != '}':
                    return False
            
        return len(stack) == 0
        