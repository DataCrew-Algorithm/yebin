#포도주 시식

'''포도주 잔을 선택하면 그 잔에 들어있는 포도주는 모두 마셔야 하고, 마신 후에는 원래 위치에 다시 놓아야 한다.
연속으로 놓여 있는 3잔을 모두 마실 수는 없다.'''

'''
6, 10, 13, 9, 8, 1 -> 6 + 10 + 9 +8 = 33 '''

#연속 3잔 불가능 -> 연속으로 두 잔, 다음 잔 건너뛰기

import sys

read = sys.stdin.readline

n = int(read())
glass = [0]

for _ in range(n):
    glass.append(int(read()))
# [0, 6, 16, 23, 22, 17, 9]

dp = [0] * (n+1)
check = [False] * (n+1)

#v1 -> 예제는 맞는데 BOJ는 틀렸대
for i in range(1,n):
    #한 잔
    if check[i-1] == False:
       dp[i] = dp[i-1] + glass[i]
       check[i] = True 
    #두 잔
    if check[i-1] == True:
        dp[i] = dp[i-1] + glass[i]
        check[i] = True
    #안마실 때
    if check[i-2] == True and check[i-1] == True:
        dp[i] = dp[i-1]
        check[i] = False
print(max(dp)) #33
