class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [ i%2 for i in nums ]
        res,cur,prefixsums = 0,0,{ 0 : 1 }
        for n in nums:
            cur += n
            res += prefixsums.get(cur - k,0)
            prefixsums[cur] =  1 + prefixsums.get(cur,0)
        return res

        