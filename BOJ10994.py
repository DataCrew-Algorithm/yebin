#BOJ10994
#별 찍기

# https://m.blog.naver.com/repeater1384/222094535029 참고

import sys

def count_star(n):
    n = int(input())
    pic = (((4 * n - 3) * 'O')+'\n') * (4 * n - 3) 
    if n == 1:
        print('*')
    else:
        count_star(n-1)
        print()


#틀을 짜준다
n = int(sys.stdin.readline())
pic = [[list((4 * n - 3) * '0')] * (4 * n - 3)]
print(pic)

#틀에 맞춰서 채워넣음
