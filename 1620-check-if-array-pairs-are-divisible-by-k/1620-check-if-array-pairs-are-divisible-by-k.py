class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        modarr = [ val%k for val in arr]
        print(modarr)
        mapp = Counter(modarr)
        print(mapp)
        if 0 in mapp and mapp[0]%2:
            return False
        for item in modarr:
            if item == 0:
                continue
            if k-item not in mapp or mapp[item] != mapp[k-item]:
                return False
             
        return True

        