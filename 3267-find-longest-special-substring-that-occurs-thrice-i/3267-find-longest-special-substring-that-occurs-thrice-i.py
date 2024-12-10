class Solution:
    def maximumLength(self, s: str) -> int:
        d = defaultdict(int)
        last = 0
        for i in range(len(s)):
            if s[i] == s[last]:
                for x in range(1,i-last+2):
                    d[s[i]*x] +=1
            else:
                d[s[i]] += 1
                last = i
        result = -1
        for each in d:
            if d[each] > 2 and len(each) > result : result = len(each)
        return result



        