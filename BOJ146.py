#editor
#스택 FILO(First In Last Out)
#append/pop

import sys

read = sys.stdin.readline

sen= (' '.join(read())).split() + ['*'] #커서 추가
# print(sen)
#['a', 'b', 'c', 'd', '*']

for _ in range(int(read())):
    c = read()
    idx = -1 #뒤에서부터 시작하니까 음수 지정
    # print(idx) ->4
    # print(c,end='')
    if len(c) == 1:
        if c == 'L': #커서 왼쪽으로 옮기기
            p = []
            for i in range(idx-1,-1):
                p.append(sen.pop())
                sen = sen + p
            #pop하고 pop해서 ['*','d'] 만들고 sen에 붙이기

    #     if c == 'D': #커서 오른쪽으로 옮기기

    #     if c == 'B': #커서 왼쪽 문자 삭제

    # if len(c) == 3:
    #     c1,c2 = map(str,c.split())
    #     if c1 == 'P':
