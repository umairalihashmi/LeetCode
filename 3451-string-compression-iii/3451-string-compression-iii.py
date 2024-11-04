class Solution:
    def compressedString(self, word: str) -> str:
        last,count = word[0], 0
        res = ""
        for i in word:
            if last != i:
                res += f"{count}{last}"
                last = i
                count = 1
            elif count > 8:
                res += f"{count}{last}"
                count = 1
            else:
                count+=1
        res += f"{count}{last}"
        return res





        