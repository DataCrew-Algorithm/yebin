#BOJ15486
#퇴사2

import sys
read = sys.stdin.readline

n = int(read())

T = []
P = []
dp = [0] * n

for i in range(n):
    t,p = map(int,read().split())
    T.append(t)
    P.append(p)
# print(T,P)
#T= [3, 5, 1, 1, 2, 4, 2] 
#P= [10, 20, 10, 20, 15, 40, 200]
#지금 날짜 + 필요한 시간 = 지금 날짜 + 들어올 수입 -> 근데 이거 못하면
#지금 날짜 = 지금 날짜 -1 (일 못하는 상태)

for i in range(n):
    if (i + T[i]) <= n:
        dp[i + T[i]] = max(dp[i],dp[i] + P[i])
    else:
        dp[i] = dp[i-1]
print(max(dp))