class Solution:
    def longestPalindrome(self, s: str) -> int:
        a = Counter(s)
        res = odd = 0
        for i in a:
            if a[i] % 2:
                odd += 1
            res += a[i]
        if odd:
            return res - odd +1
        return res - odd

        