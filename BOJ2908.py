#ver.1
'''
a = input().split()
b = a[0][::-1]
c = a[1][::-1]
if (b >= c) == True:
    print(b)
else:
    print(c) 
'''

#ver.2
a = input().split()
if (a[0][::-1] >= a[1][::-1]) == True:
    print(a[0][::-1])
else:
    print(a[1][::-1])

print(a)