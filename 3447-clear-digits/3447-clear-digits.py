class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if  47 < ord(s[i]) < 58:
                if stack:
                    stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)