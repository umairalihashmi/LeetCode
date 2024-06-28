class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        counter = defaultdict(int)
        for road in roads:
            counter[road[1]] += 1
            counter[road[0]] += 1
        x = sorted(counter.items(), key=lambda item: item[1], reverse = True)
        map = {}
        for i in range(len(x)):
            map[x[i][0]] = n-i
        result = 0
        for link in roads:
            result += (map[link[0]] + map[link[1]])
        return result
                
        