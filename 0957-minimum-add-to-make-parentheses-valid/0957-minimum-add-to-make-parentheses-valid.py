class Solution:
    def minAddToMakeValid(self, s: str) -> int:
                
        stk = []
        for b in s:
            if b == ")":
                if stk and stk[-1] == "(":
                    stk.pop()
                else:
                    stk.append(b)
            else:
                stk.append(b)
        return len(stk)
        