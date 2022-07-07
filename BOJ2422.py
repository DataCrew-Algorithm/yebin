#한윤정이 이탈리아에 가서 아이스크림을 사먹는데 
#시간초과

from itertools import combinations 
n, m = map(int,input().split())
ban = []
arr = [i for i in range(1,n+1)]
com = 0
############
icecream = list(combinations(arr, 3))

for _ in range(m):
    ban.append(list(map(int,input().split())))

for i in icecream:
    for j in ban:
        if len(set(i) & set(j)) == 2: #i 와 j 겹치는 부분(섞으면 안되는 조합) 유무 확인 
            pass
        if len(set(i) & set(j)) == 0:
            com += 1
print(com)

#윤정아 그냥 아무 맛이나 섞어 먹어