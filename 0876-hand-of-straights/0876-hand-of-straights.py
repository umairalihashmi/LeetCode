class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)
        arr = sorted(count.keys())
        # print(arr,count)
        while sum(count.values()):
            # print(count.values())
            temp = []
            for i in arr:
                # print("at:",i)
                if i in count:
                    # print(i,"found in count")
                    if count[i] > 0:
                        if temp and i != temp[-1]+1:
                            # print(i, "!=", temp[-1] +1)
                            return False
                        count[i]-=1
                        temp.append(i)
                        # print(temp)
                        # print(i,"> 0, decremented, temp:",temp, "c now--",count)
                    else:
                        # print(i,"< 0, temp remains:",temp)
                        continue 
                if len(temp) == groupSize:
                    # print(temp,"= gsize, break")
                    break
            if len(temp) < groupSize:
                # print(temp,"< g size, false")
                return False
        return True


        