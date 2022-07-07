#백설공주와 난쟁이

fake_hat =[]
new_hat = []
hat = [int(input()) for _ in range(9)]
s = sum(hat) #hat 리스트값 합치기
#조합 만들기// from itertools import combinations 사용해도 된다
for i in range(8): #0~8
    for j in range(i+1,9): #1~9// 이렇게 안하면 인덱스 초과
        if s - (hat[i] + hat[j])== 100 : #초과값 제거해서 100만들어주기
            fake_hat.append(hat[i]) #del, remove == err
            fake_hat.append(hat[j]) #새로운 리스트에 넣어준다

[new_hat.append(x) for x in hat if x not in fake_hat]  #new_hat과 fake_hat 중복 요소 삭제        
for dwarf in new_hat: #한 줄 출력
    print(dwarf)


##수빈님 답안
dwarfs = [int(input()) for _ in range(9)]         # [7, 8, 10, 13, 15, 19, 20, 23, 25] <class 'list'>

sum_dwarfs = sum(dwarfs)                            # 아홉 난쟁이의 모자의 숫자 합계

rest = sum_dwarfs - 100                             # 나머지 = 아홉 난쟁이의 모자의 숫자 합계 - 100

for i in dwarfs:
    for j in dwarfs:
        if i + j == rest and i != j and i < j:  # 두개를 골라 합이 rest와 같은 i와 j를 찾는다(단, i와 j는 같지않으며 i는 j보다 작다고 설정 (그래야 중복해서 결과가 나오지 않음))
            num1 = i
            num2 = j

dwarfs.remove(num1)  # dwarfs에서 num1, num2 제거
dwarfs.remove(num2)

for real_dwarfs in dwarfs:
    print(real_dwarfs)