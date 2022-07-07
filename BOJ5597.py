#과제 안 내신 분

num = [] #출석번호 받는 리스트
num_30 = list(range(1,31)) # 1~30번까지 받는 리스트
for _ in range(28): #출석번호 받아서 num 리스트에 추가
    num.append(int(input()))

s_not_submit = [i for i in num_30 if i not in num]
# 30번까지 있는 리스트 - 학번 받은 리스트

for n in s_not_submit:
    print(n)