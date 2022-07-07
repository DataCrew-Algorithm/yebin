#BOJ1292
#쉽게 푸는 문제

a, b = map(int,input().split())
seq = [] #sequence

for i in range(1,b+1):
    for _ in range(i):
        seq.append(i)

print(sum(seq[a-1:b]))

