class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colormap, myballs, result = defaultdict(int), defaultdict(int), [] 
        for ball, color in queries:
            temp = myballs[ball] 
            if temp:
                colormap[temp] -=1
                if not colormap[temp]: del(colormap[temp])
                myballs[ball] = color
                colormap[color] += 1
            else:
                myballs[ball] = color
                colormap[color] += 1
            result.append(len(colormap))
        return result

            