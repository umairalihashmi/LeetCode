class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = 0
        filled = numBottles
        while numBottles>=numExchange:
            total = total + filled
            filled = numBottles//numExchange
            numBottles = filled + numBottles%numExchange
        return total + filled  

        