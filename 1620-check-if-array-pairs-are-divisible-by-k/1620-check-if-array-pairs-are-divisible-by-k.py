class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        mapp = defaultdict(int)
        modarr = []
        for val in arr:
            md = val%k
            modarr.append(md)
            mapp[md] += 1
        if 0 in mapp and mapp[0]%2:
            return False
        for item in modarr:
            if item == 0:
                continue
            if k-item not in mapp or mapp[item] != mapp[k-item]:
                return False
             
        return True

        