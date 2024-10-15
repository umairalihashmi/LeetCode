class Solution:
    def minimumSteps(self, s: str) -> int:
        count = zeros = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == "1":
                count+=zeros
            else:
                zeros+=1
        return count


        