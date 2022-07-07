'''
1. split 사용해서 구하기
n = int(input()) #입력횟수
list_test = [input() for i in range(n)] #횟수만큼 입력 받아라
result = [] #띄어진 문자열('O'만 있는) 담는 리스트
S = 0 #최종점수
score = 0 
for i in list_test:
    a = i.split("X")
    result.append(a) #[['00','','00','000'],['00','','00','000']] 만들기
print(a)


'''

# 2. 'O' 없으면 도돌이표
n = int(input()) 

for i in range(n): # 아래 반복문을 n번 돌려
    S = 0 #최종점수
    score = 0 # 'X'만나기 전 점수
# input 안에 O가 있니? +1 해라. 연속으로 맞았니? 그러면 연속된 O 개수만큼 더해. O가 아니라 X가 있니? 넘겨
    for j in input():  #입력받은 문자열 내에서 반복해라
        if j == 'O': #O 있으면 +1
            score += 1
            S += score #그 문제까지 연속된 O 개수 더해
        else:
            score = 0 #없으면 스킵; 도돌이표처럼 돌아가

    print(S)