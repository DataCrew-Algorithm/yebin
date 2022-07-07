#피보나치 수2

seq = [0,1]
n = int(input())

for i in range(2,n+1):
    num = (seq[i-1] + seq[i-2])
    seq.append(num)
print(seq[n])
    
