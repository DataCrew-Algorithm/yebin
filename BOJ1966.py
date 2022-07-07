#BOJ1966
#프린터큐

import sys
from collections import deque

n =  int(sys.stdin.readline())
cnt = 1
for _ in range(n):
    lst = list(map(int,sys.stdin.readline().split())) #첫번째
    documents = deque([i for i in range(lst[0])]) #deque([0, 1, 2, 3, 4, 5])
    idx = lst[1]
    importance = deque(map(int,sys.stdin.readline().split())) #deque([1, 1, 9, 1, 1, 1])

    while importance[0] != max(importance): #중요도 가장 큰 문서가 가장 앞에 오게
        importance.rotate(-1)
        documents.rotate(-1)
        imports = importance.index(documents.index(idx))
        if importance.count(imports) == 1:  #중요도 같은 문서 없을 때
            num = sorted(importance)[imports]
        else:  #중요도 같은 문서 여러개 있을 때
            num = (documents.index(idx)) + 1
    
    print(num)
    #idx : 0 // num = documents 덱에서 숫자 0 인덱스 알려줘
    
    # print(importance)
    # print(documents)
    # # print(cnt)
    # # print(num)
 