#수 정렬

#v1
l = []
for _ in range(int(input())):
    l.append(int(input()))
    l.sort()
for i in l:
    print(i)

#v2
l = []
for _ in range(int(input())):
    l.append(int(input()))
    l.sort()

print(*l,sep="\n")