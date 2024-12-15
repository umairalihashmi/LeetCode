import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        ratiomap = defaultdict(list)
        hp = []
        for pas,total in classes:
            rat = ((pas+1)/(total+1))-(pas/total)
            ratiomap[rat].append([pas,total])
            hp.append(-rat)
        heapq.heapify(hp)
        while extraStudents:
            r = heapq.heappop(hp)
            c = ratiomap[-r].pop()
            c[0]+=1
            c[1]+=1
            extraStudents-=1
            r2 = ((c[0]+1)/(c[1]+1))-(c[0]/c[1])
            ratiomap[r2].append(c)
            heapq.heappush(hp,-r2)
            if not ratiomap[-r]: del(ratiomap[-r])    
        res = av = 0
        for each in ratiomap:
            for pas,total in ratiomap[each]:
                av +=1
                res += (pas/total)
        return res/av




        