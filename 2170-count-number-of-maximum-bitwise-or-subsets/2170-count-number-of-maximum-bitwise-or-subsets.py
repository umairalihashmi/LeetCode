class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        orr = reduce(lambda x, y: x | y, nums)
        count = 0
        def trav(arr, our):
            nonlocal count
            if not arr:
                if our == orr:
                    count+=1
                return
            trav(arr[1:],our)
            our = our | arr[0]
            trav(arr[1:],our)

        trav(nums,count)
            
        return count
        