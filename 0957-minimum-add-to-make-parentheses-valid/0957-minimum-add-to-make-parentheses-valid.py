class Solution:
    def minAddToMakeValid(self, s: str) -> int:  
        # stk = []
        # for b in s:
        #     if b == ")":
        #         stk.pop() if stk and stk[-1] == "(" else stk.append(b)
        #         continue            
        #     stk.append(b)
        # return len(stk)
        opening,closing = 0,0
        for b in s:
            if b == "(":
                opening+=1
            else:
                if opening:
                    opening-=1
                else:
                    closing+=1
        return closing + opening