class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        d = set()
        prefixsize = 0
        for item in dictionary:
            prefixsize = max(prefixsize,len(item))
            d.add(item)

        # print(d)
        # print(prefixsize)
        words = sentence.split()
        # print(words)
        for i in range (len(words)):
            for j in range(1,min(len(words[i]),(prefixsize))+1):
                # print(words[i][:j] , d)
                if words[i][:j] in d:
                    # print(words[i][:j],"in",d)
                    words[i] = words[i][:j]
        # print(words)

        # print(" ".join(words))
        return " ".join(words)
        