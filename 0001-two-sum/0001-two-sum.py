class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i,n in enumerate(nums):
            value = target-n
            if (value in nums) and nums.index(value) != i:
                return [nums.index(value),i] 