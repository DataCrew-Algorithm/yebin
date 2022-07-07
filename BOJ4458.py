#첫 글자를 대문자로

l = []
for _ in range(int(input())):
    s = input().title() #단어 첫글자 대문자로 바꾸는 함수
    s = s.replace("And","and")
    s = s.replace("Of","of")
    l.append(s)
print(*l,sep="\n")


