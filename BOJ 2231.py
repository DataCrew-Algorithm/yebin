
num = input()
#자릿수별로 나눠놓은 리스트 만들기
new_num = (" ".join(num)).split(" ")
#리스트 속 문자열 정수로 변환
new_num = [int(i) for i in new_num]
#분해합 만들기
decom = int(num) + sum(new_num)
print(decom)


#분해합을 입력값으로 받기
decom = int(input())
#분해합 생성자(N) 찾기
for n in range(1,(decom+1)):
    num = list(map(int,str(n)))
    num_sum = n + sum(num)
    if num_sum == decom:
        print(n)
        break
    if n == decom: #분해합과 생성자가 같으면 생성자가 없다는 의미
        print(0)

#분해합 216 생성자 198 예제

'''
num = (" ".join(N)).split(" ")
    num = [int(i) for i in num]
    '''