class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def reverse(x):
            return x[::-1]
        def invert(x):
            inverted_bin = ''.join('1' if bit == '0' else '0' for bit in x)
            return inverted_bin
        s = "0"
        for i in range(n):
            s = s + "1" + reverse(invert(s))
            if len(s)>= k:
                return s[k-1]
