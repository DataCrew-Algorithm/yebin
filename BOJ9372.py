#BOJ9372
#상근이의 여행

'''
상근이는 겨울방학을 맞아 N개국을 여행하면서 자아를 찾기로 마음먹었다. 

하지만 상근이는 새로운 비행기를 무서워하기 때문에, 최대한 적은 종류의 비행기를 타고 국가들을 이동하려고 한다.

이번 방학 동안의 비행 스케줄이 주어졌을 때, 상근이가 가장 적은 종류의 비행기를 타고 모든 국가들을 여행할 수 있도록 도와주자.

상근이가 한 국가에서 다른 국가로 이동할 때 다른 국가를 거쳐 가도(심지어 이미 방문한 국가라도) 된다.'''

import sys
from collections import deque

def min_plane(plane):
    cnt = 0
    country = deque([i+1 for i in range(n)])
    # for _ in range(len(country)):
    #     if lst != []:
    #         if country.popleft() in lst == True:
    #             lst.pop(lst.index(country.popleft()))
    #         cnt += 1

    # while True:
    #     lst.pop(lst.index(country.popleft()))
    #     cnt += 1
    #     if lst == []:
    #         break
    for l in lst:
        p = country.popleft()
        n_lst = []
        cnt += 1
        if lst == []:
            break
    


for t in range(int(sys.stdin.readline())):
    line1 = sys.stdin.readline().split()
    n = int(line1[0])
    m = int(line1[1])
    lst = []
    for _ in range(m):
        planes = list(map(int,sys.stdin.readline().split()))
        lst.append(planes)
print(lst)

min_plane(t)


--
import sys

n = sys.stdin.readline()

for _ in 