class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total = 0
        earlier = customers[0][0]
        for order in customers:
            earlier = max(earlier,order[0])
            earlier+=order[1]
            total = total + earlier - order[0]
        
        return total/len(customers)
        