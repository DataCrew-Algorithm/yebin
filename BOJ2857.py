l = []
ind = [] #index
for _ in range(5):
    l.append(input())

for i in l:
    if 'FBI' in i:
       ind.append((l.index(i)+1))

if len(ind) > 0:
    #ind.sort()
    ind = ' '.join(map(str, ind))
    print(ind)
else:
    print("HE GOT AWAY!")