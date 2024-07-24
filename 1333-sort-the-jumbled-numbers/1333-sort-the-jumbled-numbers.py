class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        map = defaultdict(list)
        arr = []
        for item in nums:
            x = str(item)
            ip = ""
            for digit in x:
                ip += str(mapping[int(digit)])
            ip = int(ip)
            arr.append(ip)
            map[ip].append(item)
        arr.sort()
        done = set()
        res = []
        for each in arr:
            if each in done:
                continue
            res.extend(map[each])
            done.add(each)

        return res

        