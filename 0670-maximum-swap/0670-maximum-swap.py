from sortedcontainers import SortedList        
class Solution:
    def maximumSwap(self, num: int) -> int:
        l = list(str(num))
        m = [ ( int(l[i]) ,i) for i in range(len(l)) ] 
        nums = SortedList(m)
        # print(nums)
        for i in range(len(l)):
            count, index = nums.pop()

            # print(i, l)
            if int(l[i]) < count :
                # print(l[i],"at",i, "is < ", count, "which is at",index)
                temp = l[i] 
                l[i] = str(count)
                l[index] = temp
                break
            else:
                nums.add((count,index))
                # print("heap now",nums)
                nums.discard((int(l[i]),i)) 
        # print(l)
        res = int("".join(l))
        return res

                



        # while maxHeap:
        #     count, character = heapq.heappop(maxHeap)

        #     if len(res) > 1 and res[-1] == res[-2] == character:
        #         if not maxHeap:
        #             break
        #         c2, char2 = heapq.heappop(maxHeap)
        #         res+=char2
        #         c2+=1
        #         if c2:
        #             heapq.heappush(maxHeap,(c2, char2))
        #     else:
        #         res+=character
        #         count+=1
        #     if count:
        #         heapq.heappush(maxHeap,(count,character))

        # return res


        return 0        