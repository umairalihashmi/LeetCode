class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        multiples = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                multiples[nums[i]*nums[j]] += 1
        ans = 0
        for each in multiples:
            if multiples[each] > 1 :
                ans += multiples[each]*2 * (multiples[each]-1)*2
        return ans