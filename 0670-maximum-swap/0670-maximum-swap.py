from sortedcontainers import SortedList        
class Solution:
    def maximumSwap(self, num: int) -> int:
        l = list(str(num))
        m = [ ( int(l[i]) ,i) for i in range(len(l)) ] 
        nums = SortedList(m)
        for i in range(len(l)):
            count, index = nums.pop()
            if int(l[i]) < count :
                temp = l[i] 
                l[i] = str(count)
                l[index] = temp
                break
            else:
                nums.add((count,index))
                nums.discard((int(l[i]),i)) 
        res = int("".join(l))
        return res