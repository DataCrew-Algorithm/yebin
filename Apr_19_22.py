#BOJ2748
#피보나치 수2

seq = [0,1]
n = int(input())

for i in range(2,n+1): # n>=2
    num = (seq[i-1] + seq[i-2])
    seq.append(num)
print(seq[n])
    
