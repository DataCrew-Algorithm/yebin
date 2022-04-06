#BOJ 2857
l = []
ind = [] #index
for _ in range(5): #코드네임 받기
    l.append(input())

for i in l:
    if 'FBI' in i: #FBI 있으면 ind 리스트로 인덱스 보내기
       ind.append((l.index(i)+1)) #첫번째에 있는 애 인덱스 0이니까 +1

if len(ind) > 0: #한줄로 붙여서 출력하기
    ind.sort()
    ind = ' '.join(map(str, ind))
    print(ind)
else:
    print("HE GOT AWAY!")