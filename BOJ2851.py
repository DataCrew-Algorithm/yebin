#
score = 0
mus = [int(input())for _ in range(10)]
for i in range(9): 
    score += mus[i]
    if score == 100:
        print(score)
    if score < 100 and (score + mus[i+1])>100: 
        if (abs(100 - score) < abs(100-((score + mus[i+1])))):
            print(score)
        if (abs(100 - score) > abs(100-((score + mus[i+1])))):
            print(score + mus[i+1])
        if (abs(100 - score) == abs(100-((score + mus[i+1])))):
            print(score + mus[i+1])

#
score = 0
mus = [int(input())for _ in range(10)]
for i in mus:
    score += i
    if score >= 100:
        if score - 100 > 100- (score - i): #142 - 100 > 100 - (142 - 55)
            score = score - i #142 - 55
        if score - 100 == 100- (score - i):#120 - 100 == 100 - (120 - 40)
            break
print(score)

#
score = 0
mus = [int(input())for _ in range(10)]
for i in mus:
    score += i
    if score >= 100:
        if score - 100 > 100- (score - i): #142 - 100 > 100 - (142 - 55)
            score = score - i #142 - 55
        break
print(score)