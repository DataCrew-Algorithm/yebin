#leet819
#Most common Word

class Solution:
    def mostCommonWord(self, paragraph, banned):
        punc = ",."
        for punc in punc:
            paragraph = (paragraph.lower()).replace(punc,"")
        word = paragraph.split()
        r_word = [x for x in word if x not in banned]
        lst = []
        for i in r_word:
            n = r_word.count(i)
            lst.append(n)
        return r_word[lst.index(max(lst))]

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
sol = Solution()
print(sol.mostCommonWord(paragraph, banned))
    
            