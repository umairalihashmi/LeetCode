class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        count, orr = 0,  reduce(lambda x, y: x | y, nums)
        def trav(arr, our):
            nonlocal count
            if not arr:
                count = count+1 if our == orr else count
                return
            trav(arr[1:],our)
            our = our | arr[0]
            trav(arr[1:],our)
        trav(nums,count)
        return count
        