class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        track = {0:1}
        presum = 0
        res = 0
        for i in nums:
            # print("at",i)
            presum+=i
            # print([presum])
            if abs(presum % k) in track:

                # print(abs(presum % k),"in",track)
                res+=track[abs(presum % k)]
                track[abs(presum % k)] += 1

            elif presum % k == 0:
                # print(presum % k," is 0")
                res+=1
                track[0] = 1
            else:
                # print(abs(presum % k)," not in",track)
                track[abs(presum % k)] = 1
        #     print("res at end",res)
        # print(res)
        
        return res




        