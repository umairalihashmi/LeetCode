class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        map = defaultdict(list)
        arr = []
        for s in nums:
            item = s
            ip = ""
            if item:
                while item :
                    ip = str(mapping[item%10]) + ip
                    item = item//10
            else:
                ip = str(mapping[item]) 
            ip = int(ip)
            arr.append(ip)
            map[ip].append(s)
        arr.sort()
        done = set()
        res = []
        for each in arr:
            if each in done:
                continue
            res.extend(map[each])
            done.add(each)

        return res

        