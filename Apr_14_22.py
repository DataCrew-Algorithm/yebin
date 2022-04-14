#BOJ 9655번
#돌 게임

s = int(input()) #stone
if s%2 == 1:
    print('SK')
elif s%2 ==0:
    print('CY')

'''
s가 5이상 홀수일 때: 4개가 한 단위(sk + cy) + 1 => SK
s가 6이상 짝수일 때: 6개가 한 단위(sk + cy) + 0 => CY
'''