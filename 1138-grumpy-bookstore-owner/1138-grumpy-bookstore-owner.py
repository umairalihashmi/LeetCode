class Solution:
    def maxSatisfied(self, c: List[int], g: List[int], mnt: int) -> int:
        if mnt == len(c):
            return sum(c)
        newarr = [c[i]*g[i] for i in range(len(c))]
        pfix = sum(newarr[:mnt-1])
        mx = start = 0
        for i in range(mnt-1,len(c)):
            pfix+=newarr[i]
            if pfix > mx:
                mx = pfix
            pfix -= newarr[start]
            start+=1
        ans = 0
        for i in range(len(c)):
            if not g[i]:
                ans+=c[i]
        ans+=mx
        return ans




        