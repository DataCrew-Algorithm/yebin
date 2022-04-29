#BOJ1110
#더하기 사이클

#v1 예전 풀이 76ms
#가독성 떨어지고, else 문 사용의도 알 수 없음
a = int(input())
b = a
count = 0
while True:
    if b == a%10 * 10 + (a//10 + a%10)%10:
        count = count + 1
        print(count)
        break
    else:
        a = a%10 * 10 + (a//10 + a%10)%10
        count = count + 1

#v2 80ms
num = int(input())
f_num = num
count = 0
while True:
    f_num = ((f_num % 10) * 10) + ((f_num // 10 + f_num % 10)%10)
    count += + 1
    if f_num == num:
        break
print(count)


