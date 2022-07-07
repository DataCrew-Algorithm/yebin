#저항

r = [] #resistance

color = ['black','brown','red','orange','yellow',
'green','blue','violet','grey','white']

for _ in range(3):
    idx = color.index(input()) #yellow violet red
    r.append(idx) # 4 7 2

resistance = int(str(r[0])+str(r[1])) * (10**r[2]) #('4' + '7') -> 47 * 10^2
print(resistance) #4700

#요셉님 코드
reg_color = {'black':0, 'brown':1, 'red':2, 'orange':3, 'yellow':4, 'green':5, 'blue':6, 'violet':7, 'grey':8, 'white':9}
print((10*reg_color[input()]+reg_color[input()])*10**reg_color[input()])