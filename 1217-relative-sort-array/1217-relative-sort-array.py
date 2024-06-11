class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        keycount = Counter(arr1)
        res = []
        for item in arr2:
            res.extend([item for _ in range(keycount[item])])
            del(keycount[item])
        remaining = sorted(keycount.keys())
        for item in remaining:
            res.extend([item for _ in range(keycount[item])])
        return res
        