#탄산음료

#v1
e,f,c = map(int,input().split())
s = 0 #sum
t = e + f #total
v = t//c #value
r = t%c #remainder

while t >= c:
    s += v
    t = v + r 
print(s)

#t 없애기 -> 위에서 계속 같은 수로 받으니까 무한루프

#v2
e,f,c = map(int,input().split())
s = 0 #sum
t = e + f #total
# v = t//c #value
# r = t%c #remainder

while t >= c:
    s += t//c
    t = (t//c) + (t%c) 
print(s)

'''
input = 9 0 3, s = 4
v : (9+0)//3 = 3 ... r : 0
s += v 
((9+0)//3)//3 = 1 ... 0
s += v
if v < 1:
    break
s 는 4
'''

'''
input = 5 5 2 , s = 9
v: (5+5)//2 = 5 ... r : 0
s += v
((5+5)//2)//2) = 2 ... r : 1
s += v
(((5+5)//2)//2)//2) = 1 ... r : 0
s += v
if sum(rest_bottle) != 0:
    v = (v + r)//2
s += v
print(s) 
'''
