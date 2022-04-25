#BOJ3273
#두 수의 합

#v1 시간초과
# n = int(input())
# l = input().split()
# x = int(input())
# cnt = 0

# for i in l:
#     for j in l:
#         if int(i) + int(j) == x:
#             cnt += 1
# print(cnt//2)

#v2 시간초과
# n = int(input())
# l = input().split()
# x = int(input())
# cnt = 0
# list = []

# for i in l:
#     k = (x - int(i))
#     list.append(int(k))

# for j in list:
#     if str(j) in l:
#         cnt += 1
# print(cnt//2)

#v3 시간초과
# n = input()
# l = input().split()
# x = input()
# cnt = 0

# for i in l:
#     if str(int(x) - int(i)) in l:
#         cnt += 0.5
# print(cnt)

#v4 시간초과
# n = input()
# l = input().split()
# x = input()
# for i in l:
#     if str(int(x) - int(i)) not in l:
#         l.remove(i)
# print(len(l)//2)

#힘들다...