class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = {}
        mod = 10**9 + 7
        def solve(size):
            if size in dp:   return dp[size]
            if size > high:  return 0
            if size == high: return 1
            if size >= low:
                dp[size] = (1 + solve(size + one) + solve(size + zero)) % mod 
                return dp[size] 
            dp[size] = (solve(size + one) + solve(size + zero)) % mod 
            return dp[size]
        return solve(0)