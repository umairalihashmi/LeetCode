class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        swap = 0
        for bracket in s:
            # print("bracket:",bracket,stack)
            if bracket == "]":
                if not stack:
                    stack.append("[")
                    swap+=1
                elif stack[-1] == "[":
                    stack.pop()
            else:
                stack.append(bracket)
        #     print("after bracket",stack)
        # print(stack,swap)
        # print(swap+(len(stack)//2))
        return swap