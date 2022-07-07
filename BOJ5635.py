#BOJ5635
#생일

# #v1 딕셔너리로 만들다 포기
# import sys
# n = int(sys.stdin.readline())
# for _ in range(n):
#     name, dd, mm, yy = map(str,sys.stdin.readline().split())
#     data = {'name':name, 'dd': dd, 'mm':mm, 'yy':yy}
# #{'name': 'Mickey', 'dd': 1, 'mm': 10, 'yy': 1991}

# for i in data:
#     print(list(data.values()))

#v2 딕셔너리 리스트 쓰면 안된대서 불현듯 떠오른 아이디어
import sys
n = int(sys.stdin.readline())
arc = [] #archive

for _ in range(n):
    name, dd, mm, yy = sys.stdin.readline().split()
    if len(mm) == 1:
        mm = '0'+ mm
    elif len(dd)==1:
        dd = '0' + dd
    bd = yy+mm+dd #birth day
    i = [name,bd] #info
    arc.append(i)
    arc.sort(key = lambda x:x[1])
print(arc[-1][0])
print(arc[0][0])
