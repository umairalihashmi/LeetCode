class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)
        arr = sorted(count.keys())
        while sum(count.values()):
            temp = []
            for i in arr:
                if i in count:
                    if count[i] > 0:
                        if temp and i != temp[-1]+1:
                            return False
                        count[i]-=1
                        temp.append(i)
                    else:
                        continue 
                if len(temp) == groupSize:
                    break
            if len(temp) < groupSize:
                return False
        return True


        