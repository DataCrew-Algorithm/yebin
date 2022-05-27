#BOJ16446
#콘서트
#가고싶다

#v1 532ms
import sys
n= int(sys.stdin.readline())
nums = set([i for i in range(1,n+1)])
first_ticket = set(list(map(int, sys.stdin.readline().split())))

if (nums - first_ticket) == set(): #빈 집합 나오는 경우
    print(n+1)
else:
    print(min(nums - first_ticket))

#v2 556ms

n = int(input())
nums = set([i for i in range(1,n)])
first_ticket = set(list(map(int, input().split())))

if (nums - first_ticket) == set(): #빈 집합 나오는 경우
    print(n+1)
else:
    print(min(nums - first_ticket))