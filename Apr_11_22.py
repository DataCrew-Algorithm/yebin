#BOJ 4458
#첫 글자를 대문자로

l = []
for _ in range(int(input())):
    s = input().title()
    s = s.replace("And","and")
    s = s.replace("Of","of")
    l.append(s)
print(*l,sep="\n")


