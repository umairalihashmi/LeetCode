class Solution:
    def longestPalindrome(self, s: str) -> int:
        a = Counter(s)
        res = 0
        t = False
        for i in a:
            if a[i] % 2:
                t = True
                res -= 1
            res += a[i]
        if t:
            return res+1
        return res

        