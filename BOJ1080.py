#BOJ 1080
#행렬
#그리디 알고리즘 : 선택의 순간마다 당장 눈앞에 보이는 최적의 상황만을 쫓아 최종적인 해답에 도달
import sys
read = sys.stdin.readline

n,m = map(int,read().split()) #길이/ 넓이
cnt = 0

A = []
for _ in range(n):
    A.append(list(map(int,(read().rstrip()))))
# print(A)
B = []
for _ in range(n):
    B.append(list(map(int,(read().rstrip()))))
# print(B)

for i in range(n-3): #세로
    for j in range(m-3): #가로
        if A[i][j] != B[i][j]:
            cnt +=1 
            for x in range(i,i+3): # 3X3으로 돌아다니니까  i,i+1,i+2 (i,i+3) // j,j+1,j+2 (j,j+3)
                for y in range(j,j+3):
                    if x == 0 or y == 0:
                        x = 1
                        y = 1
                    elif x == 1 or y ==1:
                        x = 0
                        y = 0

if A == B:
    print(cnt)
else:
    print(-1)



