#BOJ1874
#스택 수열

import sys

read = sys.stdin.readline

n = int(read())
original = []
# for _ in range(n):
#     original.append(int(read()))
# print(original)
#[4, 3, 6, 8, 7, 5, 2, 1]

nums1 = [] #숫자 넣어두는 리스트
nums2 = [] #숫자 빼두는 리스트
pm = [] # +/- 저장

# i = 0
# j = 1
# while i < n:
#     nums1.append(j)
#     pm.append('+')
#     j += 1
#     if original[i] == nums1[-1]:
#         nums2.append(nums1.pop())
#         pm.append('-')
#         i += 1
# print(*pm)

# for i in range(1,n+1):
#     j = 0
#     if i != original[j]: #1 != 4
#         nums1.append(i) #[1]
#         pm.append('+') #['+']
#     if i == original[j]: #4 == 4
#         nums2.append(nums1.pop()) #[1,2,3] // [4]
#         pm.append('-')
#         j += 1
# print(*pm)
'''
push 든 pop 이든 n번 돌아가야함
일일이 비교하는 게 나을수도'''

j = 1
for _ in range(n):
    org = int(read())
    original.append(org) #[4, 3, 6, 8, 7, 5, 2, 1]
    if j <= org:
        nums1.append(j)
        pm.append('+')
        j += 1
    if nums1[-1] == org:
        nums2.append(nums1.pop())
        pm.append('-')
    else:
        print('NO')


# #블로그 풀이 // 내거랑 비슷한데 while문, flag 사용 이유 모르겠어요
# n = int(input())
# stack = []
# answer = []
# flag = 0
# cur = 1
# for i in range(n):
#     num = int(input())
#     while cur <= num:       # 입력한 수를 만날 때 까지 오름차순으로 push
#         stack.append(cur)
#         answer.append("+")
#         cur += 1
#     # 입력한 수를 만나면 while문 탈출. 즉 cur = num일 때 까지 while문을 돌아 스택을 쌓는다.

#     if stack[-1] == num:    # stack의 TOP이 입력한 숫자와 같다면
#         stack.pop()         # 스택의 TOP을 꺼내 수열을 만들어 준다.
#         answer.append("-")
#     else:                   # stack의 TOP이 입력한 수가 아니면 주어진 스택을 만들 수 없다.
#         print("NO")         # 왜냐하면 12345 처럼 오름차순으로 스택이 입력되는데
#         flag = 1            # TOP이 num보다 크면 num은 TOP보다 더 아래에 쌓여있기 때문이다.
#         break               

# if flag == 0:
#     for i in answer:
#         print(i)