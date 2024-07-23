class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        x = Counter(nums)
        partmap = defaultdict(list)
        for item in x:
            partmap[x[item]].extend([item]*x[item])
        res = []
        keys = sorted(partmap.keys())
        for k in keys:
            res.extend(sorted(partmap[k],reverse = True))
        return res