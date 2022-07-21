#BOJ15649
#N & M

'''
1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열'''

import sys

read = sys.stdin.readline

n , m = map(int,read().split())

answer = []

def back_tracking():
    for i in range(1, n+1):
        if i not in answer:
            answer.append(i)
            back_tracking()
            answer.pop()
    if len(answer) == m:
        print(*answer)
back_tracking()

# from itertools import permutations
# for i in permutations(range(1, n+1), m):
#     print(*i)