class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        dummy = defaultdict(int)
        def bfs():
            res = 0
            while bfsq:
                i,j = nodes = bfsq.popleft()
                if nodes in visited or not( 0 <= i < rows and 0 <= j < cols and grid[i][j] ): continue
                visited.add(nodes)
                dummy[(i,j)] = len(islands)
                res += 1
                bfsq.extend([(i+1,j),(i-1,j),(i,j+1),(i,j-1)])
            return res
        visited = set()
        islands = []
        maxisland = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] and (i,j) not in visited:
                    bfsq = deque([(i,j)])
                    newisland = bfs()
                    islands.append(newisland)
                    if newisland > maxisland: maxisland = newisland
        for i in range(rows):
            for j in range(cols):
                if not grid[i][j]:
                    sameisland = set()
                    result = 0
                    for node in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                        if node in dummy and dummy[node] not in sameisland:
                            sameisland.add(dummy[node])
                            result += islands[dummy[node]]
                    if result >= maxisland: maxisland = result+1
        return maxisland
                    

        