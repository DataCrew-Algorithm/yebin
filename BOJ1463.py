#1로 만들기

import sys

n = int(sys.stdin.readline())

cnt = 0

# #단순구현
# while n != 1:
#     if n%3 == 0: #얘부터 계산되게 하고싶다...!
#         n = n//3
#         cnt +=1
#     if n%2 == 0:
#         n = n//2
#         cnt +=1
#     else:
#         n -= 1
#         cnt += 1
# print(cnt) # 10 -> 4

#다이나믹 프로그래밍(점화식 이용)
# https://techblog-history-younghunjo1.tistory.com/183 참고
d = [0] * (n+1) #메모제이션// n+1 안하면 인덱스 에러남
#[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(2,n+1): #d[1] = 0 이니까 2부터 시작
    d[i] = d[i-1] + 1 #1빼는 경우 // d[10] = d[9] + 1
    if i%3 == 0:
        d[i] = min(d[i],d[i//3] + 1)
    if i%2 == 0:
        d[i] = min(d[i],d[i//2] + 1)
print(d[n])

#[0,0,1,1,2,3,2,3,3,3,4]