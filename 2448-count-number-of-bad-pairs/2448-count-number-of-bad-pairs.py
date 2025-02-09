class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for i in range(len(nums)):
            count[nums[i]-i] += 1
        total = (len(nums)*(len(nums)-1))//2
        for key in count:
            if count[key] > 1:
                total -= (count[key]*(count[key]-1))//2
        return total