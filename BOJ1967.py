#BOJ 1967
#트리의 지름길

'''
트리(tree)는 사이클이 없는 무방향 그래프이다. 트리에서는 어떤 두 노드를 선택해도 둘 사이에 경로가 항상 하나만 존재하게 된다. 
트리에서 어떤 두 노드를 선택해서 양쪽으로 쫙 당길 때, 가장 길게 늘어나는 경우가 있을 것이다. 
이럴 때 트리의 모든 노드들은 이 두 노드를 지름의 끝 점으로 하는 원 안에 들어가게 된다.
이런 두 노드 사이의 경로의 길이를 트리의 지름이라고 한다. 
**정확히 정의하자면 트리에 존재하는 모든 경로들 중에서 가장 긴 것의 길이를 말한다.**

입력으로 루트가 있는 트리를 가중치가 있는 간선들로 줄 때, 트리의 지름을 구해서 출력하는 프로그램을 작성하시오. 
아래와 같은 트리가 주어진다면 트리의 지름은 45가 된다.

트리의 노드는 1부터 n까지 번호가 매겨져 있다.'''

#나의 의문: 그림으로 봤을 떄 가장 긴 경로는 7번 노드 ~ 12번 노드(간선 길이 6)인데 왜 9번 ~ 12번 노드인지?
#혹시 가중치 == 간선 한 개 당 길이라서?

#dfs -> (가장 긴 경로 찾기) -> 경로 별 가중치 더한 값 가장 큰 거 출력
#bfs -> root 노드에서 출발 -> 연결여부 확인 -> 가중치 마구 더하기 -> 가장 큰 값 출력

'''
12
부모노드 자식노드 가중치
1 2 3
1 3 2
2 4 5
3 5 11
3 6 9
4 7 1
4 8 7
5 9 15
5 10 4
6 11 6
6 12 10'''

import sys
from collections import deque

n = int(sys.stdin.readline())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n-1)]
# print(graph)
#[[1, 2, 3], [1, 3, 2], [2, 4, 5], [3, 5, 11], [3, 6, 9], [4, 7, 1], [4, 8, 7], [5, 9, 15], [5, 10, 4], [6, 11, 6], [6, 12, 10]]

#root 부터 오름차순 정렬
for i in range(len(graph)):
    graph = sorted(graph, key = lambda x:graph[i][0])
# print(graph)
# [[1, 2, 3], [1, 3, 2], [2, 4, 5], [3, 5, 11], [3, 6, 9], [4, 7, 1], [4, 8, 7], [5, 9, 15], [5, 10, 4], [6, 11, 6], [6, 12, 10]]

def bfs(s):
    visited = [-1 for _ in range(n)]
    dis = 0
    queue = deque([s])
    visited[s] = 1
    while queue:
        v = queue.popleft()
        print(graph[v])
        # for _ in graph[v]:  #<- 왜 에러나냐??????
            # e = v[1] #end
            # d = v[2] #distance
            # if visited[e] == -1:
            #     queue.append(e)
            #     visited[e] = 1
            #     dis += d
# return dis
    return

bfs(1)


# #블로그 참고
# #https://velog.io/@bae_mung/Python-BOJ-1967-트리의-지름-2
# import sys
# from collections import deque
# input = sys.stdin.readline

# def bfs(start):
#     check = [-1] * (n + 1) # 방문 체크
#     que = deque([start])
#     check[start] = 0
#     _max = [0, 0] # maxlen[0]은 해당 노드까지의 최대 거리, maxlen[1]은 해당 노드
#     while que:
#         t = que.popleft()
#         for e, w in tree[t]: # e:노드, w:거리
#             if check[e] == -1: # 해당 노드에 방문하지 않았다면
#                 que.append(e) #큐에 노드 추가
#                 check[e] = check[t] + w # 체크한 곳에 해당 거리 업데이트
#                 if _max[0] < check[e]: # 최대 거리 노드 갱신
#                     _max = check[e], e
#     return _max

# n = int(input())
# tree = [[] for _ in range(n+1)]
# for _ in range(n-1):
#     node = list(map(int, input().split())) # 부모노드, 자식노드, 웨이트가 입력됨
#     tree[node[0]].append([node[1],node[2]]) # 부모노드에 자식노드 데이터 추가
#     tree[node[1]].append([node[0],node[2]]) # 자식노드에 부모노드 데이터 추가

# dist, node = bfs(1) # 루트에서 가장 먼 노드 bfs탐색
# dist, node = bfs(node) # 루트에서 가장 먼 노드에서 가장 먼 노드 bfs탐색 -> 트리의 지름
# print(dist)