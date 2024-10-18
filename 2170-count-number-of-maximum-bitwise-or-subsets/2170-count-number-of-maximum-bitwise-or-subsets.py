class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        orr = 0
        for i in nums:
            orr = orr | i
        count = 0
        def trav(arr, our):
            nonlocal count
            if not arr:
                if our == orr:
                    count+=1
                    return
                return 
            x = trav(arr[1:],our)
            our = our | arr[0]
            z = trav(arr[1:],our)
            return
        trav(nums,count)
            

        return count
        