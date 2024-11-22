class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        map = defaultdict(int)
        for row in matrix:
            res = row
            if row[0]:
                res = [ abs(each-1) for each in row ]
            map[tuple(res)] += 1
        return max(map.values())


        