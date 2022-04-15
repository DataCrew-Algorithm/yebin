#BOJ 1076번
#저항

r = [] #resistance

color = ['black','brown','red','orange','yellow',
'green','blue','violet','grey','white']

for _ in range(3):
    idx = color.index(input()) #yellow violet red
    r.append(idx) # 4 7 2

resistance = int(str(r[0])+str(r[1])) * (10**r[2]) #('4' + '7') -> 47 * 10^2
print(resistance) #4700