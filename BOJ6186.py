#BOJ6186
#Best Grass

'''
Bessie is planning her day of munching tender spring grass and is gazing out upon the pasture 
which Farmer John has so lovingly partitioned into a grid with R (1 <= R <= 100) rows and C (1 <= C <= 100) columns. 
She wishes to count the number of grass clumps in the pasture.

Each grass clump is shown on a map as either a single '#' symbol or perhaps two '#' symbols side-by-side 
(but not on a diagonal). No two symbols representing two different clumps are adjacent. 
Given a map of the pasture, tell Bessie how many grass clumps there are.

By way of example, consider this pasture map where R=5 and C=6:'''

'''
5 6
.#....
..#...
..#..#
...##.
.#....
'''
import sys

r,c = map(int,sys.stdin.readline().split())

graph = []
for _ in range(r):
    graph.append(list(sys.stdin.readline().rstrip()))
# print(graph)

visited = [[0] * c for _ in range(r)]

from collections import deque
def bfs(x,y):
    q = deque([(x,y)])
    while q:
        x,y = q.popleft() #행렬은 xy 반대
        #상하좌우
        # direction = [(0,1),(0,-1),(-1,0),(1,0)]
        # for dir in direction:
        #     nx = x + dir[1]
        #     ny = y + dir[0]
        dx = [0,0,-1,1]
        dy = [1,-1,0,0]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx <c) and (0 <= ny < r) and (visited[ny][nx]) == 0:
                if graph[ny][nx] == '#':
                    visited[ny][nx] = 1 #방문처리
                    q.append((nx,ny))

grass = 0
for i in range(r):
    for j in range(c):
        if graph[i][j] == '#':
            if visited[i][j] == 0:
                bfs(j,i)
                grass += 1
print(grass)

#어디서 인덱스 에러?!


# #dfs 도전
# # 런타임 에러 (IndexError)
# def dfs(x,y):
#     if 0 <= x <= r and 0 <= y <= c:
#         if graph[x][y] == '.':
#             graph[x][y] = '#'
#             #상하좌우
#             direction = [(0,1),(0,-1),(-1,0),(1,0)]
#             for dir in direction:
#                 nx = x + dir[0]
#                 ny = y + dir[1]
#                 dfs(nx,ny)
#                 return True
#             return False

# result = 0
# for i in range(r):
#     for j in range(c):
#         if dfs(i,j) == True:
#             result += 1

# print(result)