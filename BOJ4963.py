#BOJ4963
#섬의 개수
'''
정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.

한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다. 

두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다. 지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.'''

#쩰리랑 비슷한 유형 -> bfs
#방향이 다양해졌다, 8가지 방향을 돌면서 연결된 섬 있으면 체크하고 방문처리 -> 방문 안 한 곳에서 다시 돌기

import sys
from collections import deque

while True:
    (w , h) = map(int,sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    m = [] # 안에 원소 개수: w
    for _ in range(h):
        m.append(list(map(int,sys.stdin.readline().split())))
    # print(m)

    #지도 개수만큼 visited 필요함
    visited = [[False] * w] * h

    #동,서,남,북,서북,서남,동북,동남
    direction = [(1,0),(-1,0),(0,-1),(0,1),(-1,1),(-1,-1),(1,1),(1,-1)]
    # dx = [1,-1,0,0,-1,-1,1,1]
    # dy = [0,0,-1,1,1,-1,1,-1]

    #섬 개수
    islet = 0

    queue = deque()
    for i in range(w):
        for j in range(h):
            if m[j][i] == 1:
                queue.append((i,j))
                #방문처리 전부 해버림
                islet += 1

                while queue:
                    a,b = queue.popleft()
                    visited[b][a] = True

                    for dx, dy in direction:
                        nx = a + dx
                        ny = b + dy
                    
                    #  #현재 위치에서 이동한 위치
                    # for i in range(8):
                    #     nx = a + dx[i]
                    #     ny = b + dy[i]
                    
                
                #지도 안에 있는 경우
                if nx >= 0 and nx <h and ny >= 0 and ny <w:
                    if not visited[ny][nx]:
                        visited[ny][nx] = True
                        queue.append([nx,ny])

    print(islet)

    
#풀이 참고1 (요셉)
# BOJ_4963 섬의 개수
from collections import deque
import sys
read = sys.stdin.readline

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]
def bfs(x, y):
    q = deque()
    q.append([x, y])
    while q:
        a, b = q.popleft()
        for i in range(8):
            X = a + dx[i]
            Y = b + dy[i]
            if 0 <= Y < h and 0 <= X < w and matrix[Y][X] == 1:
                matrix[Y][X] = 0
                q.append([X, Y])

ans = []
while True:
    w, h = map(int, read().split())
    if (w, h) == (0, 0):
        break
    matrix = [list(map(int, read().split())) for _ in range(h)]
    cnt = 0
    for row in range(h):
        for col in range(w):
            if matrix[row][col] == 1:
                bfs(col, row)
                cnt += 1
    ans.append(cnt)

for i in ans:
    print(i)


#풀이 참고2(수현)
import sys
sys.setrecursionlimit(100)
def dfs(x, y):

    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < w) and (0 <= ny < h):
            if graph[ny][nx] == 1:
                graph[ny][nx] = -1
                dfs(nx, ny)

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 & h ==0:
        break
    else:
        graph =[]
        for _ in range(h):
            tmp = list(map(int, sys.stdin.readline().split()))
            graph.append(tmp)

        cnt = 0

        for y in range(h):
            for x in range(w):
                if graph[y][x] == 1:
                    dfs(x, y)
                    cnt += 1
        # print(graph)

        print(cnt)