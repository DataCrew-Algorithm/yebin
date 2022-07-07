word = input()
censor = "CAMBRIDGE"
censoring = ([i for i in word if i not in censor])
word_censored = ''.join(censoring)
print((word_censored))