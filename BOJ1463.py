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
#d[i] = d[i-1] + d[i-2]
