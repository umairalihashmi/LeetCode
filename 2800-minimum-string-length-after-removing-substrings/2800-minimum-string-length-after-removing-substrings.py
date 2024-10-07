class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for i in s:
            stack.append(i)
            while len(stack)>= 2 and (stack[-2:] == ["A","B"] or stack[-2:] == ["C","D"]):
                stack.pop()
                stack.pop()
        return len(stack)
        