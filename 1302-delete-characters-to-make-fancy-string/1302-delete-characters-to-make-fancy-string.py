class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3: return s
        stk = [s[0],s[1]]
        for i in range(2,len(s)):
            if stk[-1] == stk[-2] == s[i]: continue
            stk.append(s[i])
        return "".join(stk)

        