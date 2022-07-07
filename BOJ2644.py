#BOJ2644
#촌수계산

'''
우리 나라는 가족 혹은 친척들 사이의 관계를 촌수라는 단위로 표현하는 독특한 문화를 가지고 있다. 
이러한 촌수는 다음과 같은 방식으로 계산된다. 기본적으로 부모와 자식 사이를 1촌으로 정의하고 이로부터 사람들 간의 촌수를 계산한다. 
예를 들면 나와 아버지, 아버지와 할아버지는 각각 1촌으로 나와 할아버지는 2촌이 되고, 아버지 형제들과 할아버지는 1촌, 나와 아버지 형제들과는 3촌이 된다.
여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때, 주어진 두 사람의 촌수를 계산하는 프로그램을 작성하시오.'''

import sys
from collections import deque


n = int(sys.stdin.readline()) #사람수
s, e = list(map(int,sys.stdin.readline().split())) #촌수 구하는 사람 s, e
m = int(sys.stdin.readline()) #관계수
graph = [[]for _ in range(n+1)]
visited = [False] * (n+1)
# print(visited)

for _ in range(m):
    x, y = map(int,sys.stdin.readline().split())
    graph[x].append(y) #그래프 추가
    graph[y].append(x) #그래프 추가
# print(graph)

#ver1 - 교재 코드 똑같이 만듦 but cnt 값이 이상함

# def bfs(v):
#     #정점, cnt
#     queue = deque((v))
#     cnt = 0
#     #현재 노드를 방문 처리
#     visited[v] = True
#     #v값이 e값이 될 때까지 반복
#     while True:
#         #원소와 cnt 뽑아
#         v = queue.popleft()
#         if v == e:
#             return cnt
#         #해당 원소와 연결된, 아직 방문하지 않은 원소들 큐에 삽입
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append((i))
#                 cnt += 1
#                 visited[i] = True
#     #다 돌았는데도 v와 e가 만나지 못한다면
#     else:
#         return -1

# print(bfs(s))

#ver2 - else 위치 수정해야할듯

# def bfs(v):
#     #정점, cnt
#     queue = deque()
#     queue.append((v,0))
#     #현재 노드를 방문 처리
#     visited[v] = True
#     #v값이 e값이 될 때까지 반복
#     while True:
#         #원소와 cnt 뽑아
#         v,cnt = queue.popleft()
#         if v == e:
#             return cnt
#         #해당 원소와 연결된, 아직 방문하지 않은 원소들 큐에 삽입
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append((i,cnt+1))
#                 visited[i] = True
#     #다 돌았는데도 v와 e가 만나지 못한다면
#     else:
#         return -1

# print(bfs(s))

#ver3

def bfs(v):
    #정점, cnt
    queue = deque()
    queue.append((v,0))
    #현재 노드를 방문 처리
    visited[v] = True
    #v값이 e값이 될 때까지 반복
    while True:
        if queue:
            #원소와 cnt 뽑아
            v,cnt = queue.popleft()
            if v == e:
                return cnt
            #해당 원소와 연결된, 아직 방문하지 않은 원소들 큐에 삽입
            for i in graph[v]:
                if not visited[i]:
                    queue.append((i,cnt+1))
                    visited[i] = True
        else:
            #다 돌았는데도 v와 e가 만나지 못한다면
            return -1
        
print(bfs(s))