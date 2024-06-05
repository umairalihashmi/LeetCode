class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        base = Counter(words[0])
        for i in range(1,len(words)):
            temp = Counter(words[i])
            for j in base:
                if j in temp:
                    if temp[j] < base[j]:
                        base[j] = temp[j]
                else:
                    base[j] = 0
        res = []
        for i in base:
            for j in range(base[i]):
                res.append(i)
        return  res