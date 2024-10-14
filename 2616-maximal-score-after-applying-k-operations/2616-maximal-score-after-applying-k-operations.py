from sortedcontainers import SortedList
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = SortedList(nums)
        res = 0
        for i in range(k):
            x = nums.pop()
            res += x
            nums.add(ceil( x / 3))
        return res