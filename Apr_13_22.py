#BOJ 1236번
#성 지키기

#v1
n = (input().split())
N = int(n[0])
M = int(n[1])
num = 0

for _ in range(N):
    c = input()
    if  c == '.' * M :
        num += 1
print(num)

#v2
n, m = map(int,input().split()) #가로, 세로
c = list(input() for _ in range(n))

row = 0 
column = 0

for i in range(n):
    if 'X' not in c[i]:
        row += 1

for j in range(m):
    for i in range(n): #i 값 설정에 문제 있는듯
        if 'X' not in c[i][j]:
            column += 1

print(min(row, column)) #값은 맞는데 틀렸다고 나온다