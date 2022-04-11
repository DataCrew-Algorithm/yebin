#BOJ 1427번
#소트인사이드

#v1
num = list(input()) #각 요소별로 리스트에 넣어준다
num.sort(reverse=True) #내림차순 정렬
print(''.join(num)) #한 문장으로 만들기

#v2
s=sorted(input())
print(''.join(s)[::-1])
