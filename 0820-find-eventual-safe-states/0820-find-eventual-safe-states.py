class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        answered = defaultdict(bool)
        visited = set()
        def issafe(node):
            if not graph[node]: return True
            if node in visited: return answered[node]
            visited.add(node)
            for next_node in graph[node]:
                if not issafe(next_node): return False
            answered[node] = True
            return True
        return [ node for node in range(len(graph)) if issafe(node)]

        