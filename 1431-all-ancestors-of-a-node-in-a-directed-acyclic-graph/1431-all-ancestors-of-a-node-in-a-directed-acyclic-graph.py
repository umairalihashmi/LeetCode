class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        x = defaultdict(set)
        dp = {}
        for edge in edges:
            x[edge[1]].add(edge[0])
        
        def getancestor(child):
            res = set()
            if child in dp:
                    return dp[child]
            if child in x:
                for parent in x[child]:
                    res.add(parent)
                    res.update(getancestor(parent))
                    dp[child] = res
            return res
        return [sorted(getancestor(i)) for i in range(n)]
        