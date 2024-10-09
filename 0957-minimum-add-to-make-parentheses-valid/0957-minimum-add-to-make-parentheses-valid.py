class Solution:
    def minAddToMakeValid(self, s: str) -> int:  
        opening = closing = 0
        for b in s:
            if b == "(":
                opening+=1
            else:
                if opening:
                    opening -= 1
                else:
                    closing += 1
        return closing + opening