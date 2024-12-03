class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res, i = "", 0
        for ind in spaces:
            while i < ind:
                res += s[i]
                i+=1
            res += " "
        return res + s[i:]
        