class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stk = []
        count = 0
        for b in s:
            if b == ")":
                if not stk:
                    count+=1
                elif stk[-1] == "(":
                    stk.pop()
                else:
                    stk.append(b)
            else:
                stk.append(b)
        return len(stk) + count
        