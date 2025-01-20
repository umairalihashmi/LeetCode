class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        row,col = len(mat), len(mat[0])
        rowsum,colsum = defaultdict(int), defaultdict(int)
        coordmap = {}
        for i in range(row):
            for j in range(col):
                coordmap[mat[i][j]] = [i,j]
        for x in range(len(arr)):
            i,j = coordmap[arr[x]]
            rowsum[i] += 1
            colsum[j] += 1
            if rowsum[i] == col or colsum[j] == row : return x
        