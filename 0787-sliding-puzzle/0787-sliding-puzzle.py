from collections import deque 
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        if board == [[1,2,3],[4,5,0]] : return 0
        bfs = deque([])
        h = len(board)
        w = len(board[0])
        count = 0
        s= tuple()
        for row in board:
            s += (tuple(row))
        seen = {s:0}
        res = float(inf)
        def move(i1,j1,i2,j2,arr):
            x = [ list(row) for row in arr ]
            x[i1][j1],x[i2][j2] = x[i2][j2],x[i1][j1]
            return x 
        def getind(arr):
            for y in range(h):
                for z in range(w):
                    if arr[y][z] == 0: return y,z
        def Bfs(arr,li,lj,i,j,count):
            if i < 0 or i >= h or j < 0 or j >= w: return
            newarr = move(li,lj,i,j,arr)
            if newarr == [[1,2,3],[4,5,0]]:
                nonlocal res
                res = min(res,count)
                return 
            s = tuple()
            for row in newarr:
                s+=(tuple(row))
            if s in seen: return
            seen[s] = count
            bfs.append([newarr,count])
        for i in range(h):
            for j in range(w):
                if board[i][j] == 0:
                    Bfs(board,i,j,i+1,j,count+1)
                    Bfs(board,i,j,i-1,j,count+1)
                    Bfs(board,i,j,i,j+1,count+1)
                    Bfs(board,i,j,i,j-1,count+1)
        while bfs:
            new,fcount = bfs.popleft()
            i,j = getind(new)
            Bfs(new,i,j,i+1,j,fcount+1)
            Bfs(new,i,j,i-1,j,fcount+1)
            Bfs(new,i,j,i,j+1,fcount+1)
            Bfs(new,i,j,i,j-1,fcount+1)
        return res if res < float(inf) else -1
        