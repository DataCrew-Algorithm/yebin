#BOJ9625
#BABBA

#내가 찾아낸 법칙: A3, B3 = A2, B2+B3
#An, Bn = B(n-1), A(n-1) + B(n-1)

seq = [(1,0)]

for i in range(1,int(input())+1):
    A = seq[i-1][1]
    B = sum(seq[i-1])
    seq.append((A,B))
print(*(seq[i]))