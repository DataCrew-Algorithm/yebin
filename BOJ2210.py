#BOJ2210
#숫자판 점프

'''
5x5 크기의 숫자판이 있다. 각각의 칸에는 숫자(digit, 0부터 9까지)가 적혀 있다. 
이 숫자판의 임의의 위치에서 시작해서, 인접해 있는 네 방향으로 다섯 번 이동하면서, 각 칸에 적혀있는 숫자를 차례로 붙이면 6자리의 수가 된다. 
이동을 할 때에는 한 번 거쳤던 칸을 다시 거쳐도 되며, 0으로 시작하는 000123과 같은 수로 만들 수 있다.
숫자판이 주어졌을 때, 만들 수 있는 서로 다른 여섯 자리의 수들의 개수를 구하는 프로그램을 작성하시오.'''

#4방향으로 다섯 번 이동 -> dfs, for 문으로 방향 바꿔가면서 함수 5번 돌리기-> str로 변환해서 붙이고 set()해서 다른 값만 남기기 -> len()
#방문확인 안해도 됨

#ver2 72ms
import sys

#그래프 그려주기
board = []
for _ in range(5):
    board.append(list(sys.stdin.readline().split()))
# print(board)

#이동할 방향 정의(상,하,좌,우)
direction = [(0,1),(0,-1),(-1,0),(1,0)]

def dfs(x,y,num,result):
    if len(num) == 6:
        result.append(num)
        return result
    
    #현재 위치에서 이동한 위치
    for dx,dy in direction:
        nx= x + dx
        ny = y + dy

        if 0 <= nx < 5 and 0<= ny < 5:
            dfs(nx,ny,num+board[nx][ny],result)

def tada():
    result = []
    for i in range(5):
        for j in range(5):
            dfs(i,j,board[i][j],result)
    return result

#중복 ㄴㄴ -> set
print(len(set(tada())))

#ver1 ver2 차이 -> direction 위치