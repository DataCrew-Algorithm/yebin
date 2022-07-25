#BOJ9095
#1,2,3 더하기

import sys

read = sys.stdin.readline

dp = [0, 1, 2, 4, 0, 0, 0, 0, 0, 0, 0] #n <11

for i in range(4,11):
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
# print(dp)

for _ in range(int(read())):
        print(dp[int(read())])
        
# 1:1, 2:2, 3:4, 4:7, 5:13
# dp[4] = dp[1] + dp[2] + dp[3]
#dp[5] = dp[2] + dp[3] + df[4]
#dp[i] = dp[i-3] + dp[i-2] + dp[i-1]


