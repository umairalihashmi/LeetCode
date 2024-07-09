class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total = 0
        start = customers[0][0]
        for order in customers:
            if start < order[0]:
                start = order[0]
            start += order[1]
            total = total + start - order[0]
        return total/len(customers)
        