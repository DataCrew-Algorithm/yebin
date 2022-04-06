num = []
num_30 = list(range(1,31))
for _ in range(28):
    num.append(int(input()))

s_not_submit = [i for i in num_30 if i not in num] #num_30 - num = 리스트 간 차이

for n in s_not_submit:
    print(n)