class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        x = defaultdict(set)
        for edge in edges:
            x[edge[1]].add(edge[0])
        dp = {}
        def getancestor(child):
            res = set()
            if child in x:
                if child in dp:
                    return dp[child]
                for parent in x[child]:
                    res.add(parent)
                    res.update(getancestor(parent))
                    dp[child] = res
            return res
        result = []
        for i in range(n):
            result.append(sorted(getancestor(i)))
        return result
        