class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = Counter(nums)
        x = 0
        for i in range(3):
            for _ in range(c[i]):
                nums[x] = i
                x = x + 1