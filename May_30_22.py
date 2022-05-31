from collections import deque
import sys
queue = deque()

for _ in range(int(sys.stdin.readline())):
    c = sys.stdin.readline().split() #push 1 [push,1]
    if c[0] == 'push':
        c[1] = int(c[1])
        queue.append(c[1])
    if c[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else: print(queue.popleft())
    if c[0] == 'size':
        print(len(queue))
    if c[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    if c[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    if c[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])