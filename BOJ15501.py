#BOJ15501
#부당한 퍼즐

#v1
# import sys
# from collections import deque

# n =  int(sys.stdin.readline())
# lst1 =  deque(sys.stdin.readline().split())
# lst2 = deque(sys.stdin.readline())

# while True:
#     lst2.appendleft(lst2.popleft())
#     if lst2 == lst1 or lst2 == reversed(lst1):
#         break
# print('good puzzle')

#  #아닌 경우는 어떻게 구해

#v2
# import sys
# n =  int(sys.stdin.readline())
# lst1 =  sys.stdin.readline().split()
# lst2 =  sys.stdin.readline().split()

# k = lst2.index('1')
# for i in range(k,n-1):
#     lst2.insert(0,lst2.pop())

# if lst1 == lst2:
#     print('good puzzle')
# elif lst1 == reversed(lst2) :
#     print('good puzzle')
# else:
#     print('bad puzzle')

#v3
# import sys
# n =  int(sys.stdin.readline())
# lst1 =  sys.stdin.readline().split()
# lst2 =  sys.stdin.readline().split()

# k = lst2.index('1')
# for i in range(k,n-1):
#     lst2.insert(0,lst2.pop())
# lst2.reverse()
# if lst2 == lst1:
#     print('good puzzle')
# else:
#     print('bad puzzle')

#v4 22.06.20

'''
플레이어는 1 ~ n 까지 숫자가 한 번씩만 나타나는 수열을 하나 가지고 시작한다.
또 다른 1 ~ n 까지 숫자가 한 번씩만 나타나는 수열이 주어졌을 때, 처음 수열을 적절히 변형해서 처음 받은 수열을 이 수열과 동일한 수열로 만들어야 한다.
이때, 플레이어가 수열에 대해서 할 수 있는 동작은 다음 두 가지가 있다. 동작은 몇 번이라도 수행할 수 있다.
뒤집기 : 현재 수열을 거꾸로 뒤집는다. ex) 1 2 3 4 5 -> 5 4 3 2 1
밀기 : 현재 수열을 왼쪽 혹은 오른쪽으로 한 칸 민다. ex) 1 2 3 4 5 -> 5 1 2 3 4'''

import sys
from collections import deque

n = int(sys.stdin.readline())
lst1 = deque(sys.stdin.readline().split())
lst2 = deque(sys.stdin.readline().split())

for _ in range(n):
    if lst1 == lst2 or deque(reversed(lst1)) == lst2:
        print('good puzzle')
        break
    lst1.rotate(1)
else:
    print('bad puzzle')
