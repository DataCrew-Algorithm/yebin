#BOJ2606
#바이러스

from collections import deque
import sys


computer = int(sys.stdin.readline())
connection = int(sys.stdin.readline())
graph = [[]for _ in range(computer+1)]
visited = [False] * (computer+1)
cnt = 0

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    #Queue 빌 때까지
    while queue:
        #방문한 노드 큐에서 추출
        v = queue.popleft()
        print(v,end=' ')
        #방문 안한 노드 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
        cnt += 1
                
for _ in range(connection):
    i,j = map(int,sys.stdin.readline().split())
    #방문했다
    graph[i][j] = graph[j][i] = True

print(graph)

bfs(graph,1,visited)
print(cnt -1)