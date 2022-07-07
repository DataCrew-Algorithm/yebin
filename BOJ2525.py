#오븐 시계

h,m = map(int,input().split())
plus_t = int(input())

if m + plus_t >= 60:
    h += ((m + plus_t)//60)
    m = (m + plus_t) - (60 *((m + plus_t)//60))
    if h > 23: #24시 이상
        h = h - 24
    print(h,m)
else:
    m += plus_t
    print(h,m)