class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        base = Counter(words[0])
        for i in range(1,len(words)):
            temp = Counter(words[i])
            for j in base:
                if j in temp:
                    if base[j] > temp[j]:
                        base[j] = temp[j]
                else:
                    base[j] = 0
        res = []
        for i in base:
            if base[i]:
                res.extend([ i for j in range(base[i])])
        return  res

        