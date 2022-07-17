#회장뽑기

#전에 풀었던 2- 친구 느낌으로 풀면 될 듯?

# #플로이드 워셜 알고리즘
# for i in range(n): #거쳐가는 점
#     for j in range(n): #시작점
#         for k in range(n): #끝점
#             if j == k: #시작점 == 끝점인 경우
#                 continue
#             if graph[j][k] == 'Y' or (graph[j][i] == 'Y' and graph[i][k] == 'Y'): #직통 or 경유
#                 visited[j][k] = 1
# # print(visited) #2-친구 리스트
# friend = []
# for i in visited: #다 더해버려
#     friend.append(sum(i))
# print(max(friend))


import sys

n = int(sys.stdin.readline())

graph = [[0] * (n+1) for _ in range(n+1)] #여기서 에러?
# print(graph)

visited = [[-1] for _ in range(n)]

while True: 
    i,k = map(int,sys.stdin.readline().split())
    if (i,k) == (-1,-1):
        break
    graph[i][k] = 1
    graph[k][i] = 1
print(graph)


for i in range(1,n+1): 
    for j in range(1,n+1):
        for k in range(1,n+1):
            if j == k: #시작점 == 끝점인 경우
                continue
            if graph[j][k] == 0 or (graph[j][i] == 0 and graph[i][k] == 0): #직통 or 경유
                visited[j][k] += 1
print(visited)
s = min(visited)
print(len(s), s)




# #블로그참고
# from collections import deque

# def bfs(n):
#     visited = [-1] * (N+1)
#     visited[n] = 0
#     Q = deque([n])
#     while Q:
#         v = Q.popleft()
#         for w in adj[v]:
#             if visited[w] == -1:
#                 visited[w] = visited[v] + 1
#                 Q.append(w)
#     return max(visited)

# N = int(input())
# adj = [[] for _ in range(N+1)]
# while True:
#     a, b = map(int, input().split())
#     if a == -1 and b == -1:
#         break
#     adj[a].append(b)
#     adj[b].append(a)

# score = 50
# lst = []

# for n in range(1, N+1):
#     tmp = bfs(n)
#     if tmp < score:
#         score = tmp
#         lst = [n]
#     elif tmp == score:
#         lst.append(n)
# print(score, len(lst))
# print(*lst)