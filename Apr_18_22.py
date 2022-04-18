#BOJ1292
#쉽게 푸는 문제

a, b = map(int,input().split())
seq = [] #sequence

for i in range(b):
    for _ in range(i):
        seq.append(i)
        s = sum(seq[a-1:b])

print(s)
