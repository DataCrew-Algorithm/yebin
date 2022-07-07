#v1
s = list(input())
s.sort(reverse=True)
print(''.join(s))

#v2
s=sorted(input())
print(''.join(s)[::-1])
