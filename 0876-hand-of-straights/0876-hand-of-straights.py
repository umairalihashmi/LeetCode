class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        # print(hand)
        if len(hand) % groupSize:
            return False
        for i in range((len(hand)//groupSize)+1):
            if 0 <= len(hand)-hand.count(-1) < groupSize:
                break 
            t = 0
            while t < len(hand) and hand[t] == -1:
                t+=1
            # print("t went to :",t)
            # if hand[-1] == -1:
            #     break
            temp = []
            for i in range(t,len(hand)):
                # print("index:",i,temp,hand)
                if len(temp) == groupSize:
                    break
                if temp and temp[-1] == hand[i]:
                    continue
                if hand[i] == -1:
                    continue
                if temp and temp[-1] != hand[i]-1:
                    # print(temp," and not consecutive :",temp[-1],hand[i]-1)
                    continue
                
                temp.append(hand[i])
                hand[i] = -1
                # print("hand:",hand)
            if len(temp) < groupSize:
                # print(len(temp),"< gsize")
                return False
        for i in hand:
            if hand[i] > -1:
                return False
        return True