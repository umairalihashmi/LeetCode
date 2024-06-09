class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        track = {0:1}
        presum = 0
        res = 0
        for i in nums:
            presum+=i
            modd = abs(presum % k) 
            if modd in track:
                res+=track[modd]
                track[modd] += 1
                continue
            elif modd == 0:
                res+=1
            track[modd] = 1
        return res




        