#BOJ1058
#친구

'''
지민이는 세계에서 가장 유명한 사람이 누구인지 궁금해졌다. 가장 유명한 사람을 구하는 방법은 각 사람의 2-친구를 구하면 된다. 
어떤 사람 A가 또다른 사람 B의 2-친구가 되기 위해선, 두 사람이 친구이거나, A와 친구이고, B와 친구인 C가 존재해야 된다. 
여기서 가장 유명한 사람은 2-친구의 수가 가장 많은 사람이다. 가장 유명한 사람의 2-친구의 수를 출력하는 프로그램을 작성하시오.

A와 B가 친구면, B와 A도 친구이고, A와 A는 친구가 아니다.'''

#첫째 줄에 사람의 수 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 각 사람이 친구이면 Y, 아니면 N이 주어진다.

#dfs -> 그래프 전부 탐색 -> 노드별로 가지 개수 저장 -> 제일 큰 숫자 출력

# import sys
# # sys.setrecursionlimit(10000)

# n = int(sys.stdin.readline())
# graph = []
# for _ in range(n):
#     graph.append(list(sys.stdin.readline().rstrip()))
# # print(graph)
# #[['N', 'Y', 'Y'], ['Y', 'N', 'Y'], ['Y', 'Y', 'N']]

# visited = [False for i in range(n)]
# # print(visited)

# def dfs(v):
#     for i in range(n):
#         #방문 안했고, 친구 Y면 방문처리 레고
#         if visited[i] == False and graph[v][i] == 'Y':
#             visited[i] = True
#             dfs(i)

# for i in range(n):
#     dfs(i)
#     for j in range(n):
#         if visited[j] == True:
#             print(1, end=' ')
#         else:
#             print(0, end=' ')
#     print()
#     #visited 초기화
#     visited = [False for i in range(n)]

# #ver2 - bfs 출력 안됨
# import sys
# from collections import deque

# n = int(sys.stdin.readline())

# graph = []
# for _ in range(n):
#     graph.append(list(sys.stdin.readline().rstrip()))


# def bfs(a):
#     #초기화되어야하니까
#     visited = ([False] * n) * n
#     # print(visited)   
#     q = deque([(a,0)])
#     visited[a] = True
#     f = 0
#     while q:
#         v = q.popleft()
#         # print(q)
#         q.append(v)
#         for i in range(n):
#             if graph[v][i] == 'Y' and visited[i] == False:
#                 q.append(i)
#                 visited[i] = True
#         f += 1
#     return f -1

# for i in range(n):
#     friend = bfs(i)
#     print(friend)

#ver3 -Floyd 
# https://freedeveloper.tistory.com/385 참고
import sys

n = int(sys.stdin.readline())
graph = []
for _ in range(n):
    graph.append(list(sys.stdin.readline().rstrip()))
# print(graph)

visited = [[0 for _ in range(n)] for _ in range(n)] #T/F로 하면 마지막에 꼬인다 -> 0/1 변환

#플로이드 워셜 알고리즘
for i in range(n): #거쳐가는 점
    for j in range(n): #시작점
        for k in range(n): #끝점
            if j == k: #시작점 == 끝점인 경우
                continue
            if graph[j][k] == 'Y' or (graph[j][i] == 'Y' and graph[i][k] == 'Y'): #직통 or 경유
                visited[j][k] = 1
# print(visited) #2-친구 리스트
friend = []
for i in visited: #다 더해버려
    friend.append(sum(i))
print(max(friend))