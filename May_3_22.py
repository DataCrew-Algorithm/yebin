#Most common Word
#v1 'run != submit'
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
    
#v2 60ms
class Solution:
    def mostCommonWord(self, paragraph, banned):
        punc = ",.!'?;`'" #비효율적 -> 정규표현식 사용하는거 추천
        for punc in punc:
            paragraph = (paragraph.lower()).replace(punc," ")
        word = paragraph.split()
        r_word = [x for x in word if x not in banned]
        lst = []
        for i in r_word:
            n = r_word.count(i)
            lst.append(n)
        return r_word[lst.index(max(lst))]

paragraph = "a, a, a, a, b,b,b,c, c"
banned = ["a"]
sol = Solution()
print(sol.mostCommonWord(paragraph, banned))