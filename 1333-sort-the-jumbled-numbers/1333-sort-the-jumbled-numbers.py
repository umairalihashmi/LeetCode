class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        map = defaultdict(list)
        arr = []
        for s in nums:
            ip = ""
            if s:
                item = s
                while item :
                    ip = str(mapping[item%10]) + ip
                    item = item//10
            else:
                ip = str(mapping[s]) 
            ip = int(ip)
            arr.append(ip)
            map[ip].append(s)
        arr.sort()
        done = set()
        res = []
        for each in arr:
            if each in done:
                continue
            done.add(each)
            res.extend(map[each])

        return res

        