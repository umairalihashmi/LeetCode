class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        moves = 0
        for i in range(1,len(nums)):
            if nums[i] <= nums[i-1]:
                next = nums[i-1] + 1
                moves = moves + next - nums[i]
                nums[i] = next
        return moves
        