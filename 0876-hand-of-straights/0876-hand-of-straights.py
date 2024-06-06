class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        if len(hand) % groupSize:
            return False
        for i in range((len(hand)//groupSize)+1):
            if 0 <= len(hand)-hand.count(-1) < groupSize:
                break 
            t = 0
            while t < len(hand) and hand[t] == -1:
                t+=1
            temp = []
            for i in range(t,len(hand)):
                if len(temp) == groupSize:
                    break
                elif temp and temp[-1] == hand[i]:
                    continue
                elif hand[i] == -1:
                    continue
                elif temp and temp[-1] != hand[i]-1:
                    continue
                temp.append(hand[i])
                hand[i] = -1
            if len(temp) < groupSize:
                return False
        for i in hand:
            if hand[i] > -1:
                return False
        return True