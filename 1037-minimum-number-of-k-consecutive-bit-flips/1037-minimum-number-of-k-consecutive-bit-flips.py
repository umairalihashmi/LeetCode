class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)-k+1):
            if not nums[i]:
                res+=1
                for j in range(i,i+k):
                    nums[j] = abs(nums[j]-1) 
                # print("arrray becomes",nums,"at",i)
        # print(nums[len(nums)-k:])
        if sum(nums[len(nums)-k:]) < k:
            return -1
        # if nums[-k:]
        return res
        