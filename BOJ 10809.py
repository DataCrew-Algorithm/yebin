S = input()
al = "abcdefghijklmnopqrstuvwxyz"
S_index = [S.find(i) for i in al]
result = ' '.join(str(x) for x in S_index)
print(result)