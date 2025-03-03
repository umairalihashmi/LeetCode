class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left,right,middle = [],[],[]
        for val in nums:
            if val < pivot: left.append(val)
            elif val > pivot: right.append(val)
            else: middle.append(val)
        return left + middle + right