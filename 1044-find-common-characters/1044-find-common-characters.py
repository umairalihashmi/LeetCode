class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) == 1:
            return list(words[0])
        base = Counter(words[0])
        for i in range(1,len(words)):
            temp = Counter(words[i])
            for j in temp:
                if j in base and base[j]:
                    base[j] = min(base[j],temp[j])
            for d in base:
                if d not in temp:
                    base[d] = 0
        res = []
        for i in base:
            if base[i]:
                res.extend([ i for j in range(base[i])])

        return  res

        