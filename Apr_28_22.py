#BOJ5800
#성적 통계
import sys
n = int(sys.stdin.readline())
g = [] #gaps
for i in range(n):
    data = list(map(int,(sys.stdin.readline().split())))
    #student = int(data[0])
    score = sorted(data[1:],reverse=True) #점수들 내림차순 정리
    for j in range(len(score)-1): #차이 구하기
        g.append(score[j]- score[j+1])
    print('Class '+ str(i+1))
    print('Max '+ str(score[0]) +', Min ' + str(score[-1]) + ', Largest gap ' + str(max(g)))
    g.clear() #append 해놓은 리스트 비워놓기 -> 그래야 재사용가능

#출력 문구 space 주의!!!
# print('a'+'b') ->  ab
# print('a','b') -> a b