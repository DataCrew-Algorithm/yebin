n = int(input())
can1 = []
can2 = []
can3 = []
l= []
for i in range(n):
    a= input().split()
    can1.append(a[0])
    can1 = list(map(int,can1))
    can2.append(a[1])
    can2 = list(map(int,can2))
    can3.append(a[2])
    can3 = list(map(int,can3))
can1 = sum(can1)
can2 = sum(can2)
can3 = sum(can3)
l = [can1,can2,can3]

if l.count(max(l)) == 1:
    print(l.index(max(l))+1,max(l))
else:
    print(0,max(l))