class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rowmap,colmap = defaultdict(list),defaultdict(list)
        count = 0
        alone = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    count += 1
                    rowmap[i].append((i,j))
                    colmap[j].append((i,j))
        for row in rowmap:
            if len(rowmap[row]) == 1:
                if len(colmap[rowmap[row][0][1]]) == 1:
                    alone.add(rowmap[row][0])
        for col in colmap:
            if len(colmap[col]) == 1:
                if len(rowmap[colmap[col][0][0]]) == 1:
                    alone.add(colmap[col][0])
        return count - len(alone)