#BOJ 2667
#단지 번호 붙이기

'''
<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 
철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 
여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 
대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 
지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.'''

#dfs -> 섬 문제처럼 풀이 -> 정렬 -> len()



import sys
# sys.setrecursionlimit(100000)

n = int(sys.stdin.readline())

cnt = 0 #cnt: 집 개수
#map
m = [list(sys.stdin.readline()) for _ in range(n)] #int로하면 0 날아감
# print(m)

#dfs
def dfs(x,y):
    global cnt
    #상하좌우(x,y)
    direction = [(0,1),(0,-1),(-1,0),(1,0)]
    #현재 위치에서 이동한 위치
    for dx,dy in direction:
        nx= x + dx
        ny = y + dy
        #범위안에 있고 집일 때
        if (0 <= nx < n) and (0 <= ny < n):
            if m[ny][nx] == '1':
                m[ny][nx] = 0
                cnt += dfs(nx,ny)
        return cnt + 1

#ville은 단지 모음
ville = []
for i in range(n):
    for j in range(n):
        if m[i][j] == '1':
            ville.append(dfs(i,j))

print(len(ville)) #15? why ?



#블로그 참고
# def dfs(x,y): 
#     global cnt 
#     if x<=-1 or x>=N or y<=-1 or y>=N: 
#         return False 
#     #방문하지않은 노드 방문처리하고 인접노드에 대해서 방문 
#     if graph[x][y] == 1: 
#         graph[x][y] = 0 
#         cnt += 1 
#         #인접노드 방문 
#         dfs(x-1,y) 
#         dfs(x+1,y) 
#         dfs(x,y-1) 
#         dfs(x,y+1) 
#         return True 
#     return False     


# N = int(input()) 
# graph = [] 
# global cnt 
# cnt = 0 
# danzi_n = 0 
# danzi_cnt = [] 
# for i in range(N): 
#     graph.append(list(map(int,input()))) 

# for i in range(N): 
#     for j in range(N): 
#         # 정사각형 각 정점에 대해서 
#         flag = dfs(i,j) 
#         if flag == True: 
#             danzi_n += 1 
#             danzi_cnt.append(cnt) 
#             cnt = 0 

# danzi_cnt.sort() 
# print(danzi_n) 
# for i in danzi_cnt: 
#     print(i) 