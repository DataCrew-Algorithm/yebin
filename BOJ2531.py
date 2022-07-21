#BOJ2531
#회전 초밥


import sys
from collections import deque
read = sys.stdin.readline

#접시 / 가짓수 / 연속접시 / 초밥 쿠폰
n,d,k,c = map(int,read().split())
# print(n,d,k,c)

belt = deque([])
for _ in range(n):
    belt.append(int(read()))
# print(belt)
#[7, 9, 7, 30, 2, 7, 9, 25]

sushi = [] #먹을 수 있는 초밥
cnt = 0

#deque
for _ in range(n):
    for i in range(k): #4번 넣어주기
        if belt[i] not in sushi:
            sushi.append(belt[i])
            cnt = len(sushi)
        if len(sushi) == k:
            ans = cnt
    belt.rotate() #돌려서
    if c not in sushi:
        ans += 1
print(ans)

# #two pointer(블로그 참고: https://ryu-e.tistory.com/33)
# import sys
# from collections import defaultdict

# # 접시 수, 초밥 가짓수, 연속해서 먹는 접시 수, 쿠폰 번호
# n, d, k, c = map(int, sys.stdin.readline().split())
# arr = [int(sys.stdin.readline()) for _ in range(n)]
# arr.extend(arr)   # 원형이라서 2개를 이어준다.
# left = 0
# right = 0
# dict_ = defaultdict(int)
# result = 0

# dict_[c] += 1          # 보너스는 무조건 먹기 

# # 1. 처음에 k 구간만큼 먹기
# while right < k:
#     dict_[arr[right]] += 1
#     right += 1

# # 2. 슬라이딩 윈도우 적용 
# while right < len(arr):
#     result = max(result, len(dict_))
#     # 1. 맨 왼쪽 초밥 제거
#     dict_[arr[left]] -= 1
#     if dict_[arr[left]] == 0:  # 삭제된 왼쪽 초밥이 0 이면 dict 삭제 
#         del dict_[arr[left]]
#     # 2. 오른쪽 초밥 추가하기 
#     dict_[arr[right]] += 1
#     # 왼쪽 위치 + 1
#     left += 1
#     # 오른쪽 위치 + 1
#     right += 1

# print(result)