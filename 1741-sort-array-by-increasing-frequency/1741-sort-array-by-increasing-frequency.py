class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        x = Counter(nums)
        res = []
        # print(x)
        partmap = defaultdict(list)
        for item in x:
            partmap[x[item]].extend([item]*x[item])
        # print(partmap)
        k = sorted(partmap.keys())
        for keys in k:
            partmap[keys].sort(reverse = True)
            res.extend(partmap[keys])

        return res
        