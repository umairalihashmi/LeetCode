class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [ i for i in range(1,n+1)]
        while len(arr)>1:
            ind = (k%len(arr)) 
            if not ind:
                arr.pop()
            else:
                arr = arr[ind:] + arr[:ind-1]
        return arr[0]      