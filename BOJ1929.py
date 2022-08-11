#소수

# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

import sys
read = sys.stdin.readline

m,n = map(int,read().split())

# #v1 : 시간초과 and 코드 더러움!
# nums = []
# for i in range(m,n+1): #3부터 16까지 자연수
#     lst = []
#     for j in range(1,i+1): #1부터 i까지 자연수
#         if i % j == 0: #i가 나누어 떨어질 때
#             lst.append(j)
#     nums.append(lst)
# # print(nums) #[[1, 3], [1, 2, 4], [1, 5], [1, 2, 3, 6], [1, 7], [1, 2, 4, 8], [1, 3, 9], [1, 2, 5, 10], [1, 11], [1, 2, 3, 4, 6, 12], [1, 13], [1, 2, 7, 14], [1, 3, 5, 15], [1, 2, 4, 8, 16]]
# prime = [i for i in nums if len(i) == 2]
# # print(prime) #[[1, 3], [1, 5], [1, 7], [1, 11], [1, 13]]

# for i in prime:
#     print(i[1])

#v2 : 시간초과
for i in range(m,n+1): #3부터 16까지 자연수
    prime = []
    for j in range(1,i+1): #1부터 i까지 자연수
        if i % j == 0: #i가 나누어 떨어질 때
            prime.append(j)
    if len(prime) ==2:
        print(prime[1])


##########################################################
# 인터넷에서 찾은 에라토스테네스의 체
def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]