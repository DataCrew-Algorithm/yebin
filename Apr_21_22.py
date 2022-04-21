#BOJ5086
#배수와 약수

f = ()
s = ()
while f != 0 and s != 0:
    f, s = map(int,input().split())
    if f > s:
        if f % s == 0:
            print('multiple')
        else:
            print('neither')
    
    elif s > f:
        if s % f == 0:
            print('factor')
        else:
            print('neither')

#마지막에 입력하는 0 0 은 break 역할인가?