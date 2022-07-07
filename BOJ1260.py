#BOJ1260
#DFS & BFS

import sys
import collections
from collections import deque

visited=[]
graph = collections.defaultdict(list)
queue = deque()

n , m , v = map(int,sys.stdin.readline().split())
for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start,visited):
    visited.append(start)
    for i in sorted(graph[start]):
        if i not in visited:
            visited.append(i)
            dfs(i,visited)
    return visited

def bfs(start,visited):
    visited.append(start)
    queue.append(start)
    while queue:
        v = queue.popleft()
        for i in sorted(graph[v]):
            if i not in visited:
                visited.append(i)
                queue.append(i)
                bfs(i,visited)
    return visited

print(*dfs(v,visited))
print(*bfs(v,visited))
