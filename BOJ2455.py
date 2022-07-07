l = []
m = []
p = 0
k = 1
num_p = 0

for i in range(4):  #기차역 개수만큼 반복
    l = l + input().split() #내린사람 탄사람 구분 리스트
    #print(l) : ['0', '32', '3', '13', '28', '25', '39', '0']
    l = list(map(int,l))
    #print(l) : [0, 32, 3, 13, 28, 25, 39, 0]
    num_p = num_p - l[p] + l[k] #총 인원 계산
    m.append(num_p) # 총 인원수 담은 리스트 만들기
    p += 2 #짝수번째 인덱스(내린 사람)
    k += 2 #홀수번째 인덱스(탄 사람)
print(max(m)) #최대값