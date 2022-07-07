#BOJ10773
#제로
import sys

n = int(sys.stdin.readline()) #sys 굳이 input()
data = [sys.stdin.readline().strip() for i in range(n)]
l = []

#스택 전형적인 풀이방법 참고
for i in data:
    l.append(i)
    if 0 in l:
        del l[-1]
print(l)

del data[-1]
print(data)