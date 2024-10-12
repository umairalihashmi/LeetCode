class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = [-1 for i in range(len(nums))]
        for idx,item in enumerate(nums):
            for i in range(item):
                if (i | (i+1)) == item:
                    ans[idx] = i
                    break
        return ans
        