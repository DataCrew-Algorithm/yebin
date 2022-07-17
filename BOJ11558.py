#BOJ11558
#The Game Of Death

#ex
# 1(h) -> 2 -> 3 -> 4 -> 5 -> 6 -> 7(j) -> 1

import sys

def dfs(s):
    # visited[s] = 1
    for i in player[s]:
        if visited[i] == 0:
            visited[i] = visited[s] + 1 #이 부분만 다름/이해 안 됨?!
            dfs(i)
                
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    player = [[] for _ in range(n+1)] #각 테스트 케이스마다 리스트 갱신
    visited = [0] * (n+1)
    for i in range(1,n+1):
        a = int(sys.stdin.readline())
        player[i].append(a)
    dfs(1)
    #여기는 블로그 코드
    if visited[i] != 0:
        print(visited[i])
        print(visited)
        #[0, 7, 1, 2, 3, 4, 5, 6]
    else:
        print(visited)
        print(0)
