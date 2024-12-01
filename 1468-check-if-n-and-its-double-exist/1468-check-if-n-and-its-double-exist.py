class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        dict = {arr[i]: i for i in range(len(arr))}
        for i in range(len(arr)):
            x = arr[i] * 2 
            if x in dict and dict[x] != i :
                return True  
        return False  