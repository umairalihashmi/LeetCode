from sortedcontainers import SortedList
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        a = SortedList(nums)
        res = 0
        for i in range(k):
            x = a.pop()
            res += x
            a.add(ceil( x / 3))
        return res