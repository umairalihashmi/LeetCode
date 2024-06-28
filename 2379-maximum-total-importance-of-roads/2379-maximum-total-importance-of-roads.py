class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        counter = defaultdict(int)
        result = 0
        for road in roads:
            counter[road[1]] += 1
            counter[road[0]] += 1
        x = sorted( [[counter[key],key] for key in counter], reverse = True )
        map = { x[i][1] : n-i for i in range(len(x)) }
        for link in roads:
            result = result + map[link[0]] + map[link[1]]
        return result
                
        