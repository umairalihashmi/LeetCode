class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [ i%2 for i in nums ]
        res = cur = 0
        prefixsums = { 0 : 1 }
        for n in nums:
            cur+=n
            diff = cur - k
            res += prefixsums.get(diff,0)
            prefixsums[cur] =  1 + prefixsums.get(cur,0)
        return res

        