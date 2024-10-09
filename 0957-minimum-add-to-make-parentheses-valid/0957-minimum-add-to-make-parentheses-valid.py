class Solution:
    def minAddToMakeValid(self, s: str) -> int:  
        stk = []
        for b in s:
            if b == ")":
                stk.pop() if stk and stk[-1] == "(" else stk.append(b)
                continue            
            stk.append(b)
        return len(stk)
        