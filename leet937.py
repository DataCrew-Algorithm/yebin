#로그 가장 앞 부분은 식별자다
#문자로 구성된 로그가 숫자 로그보다 앞에 온다
#식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다
#숫자 로그는 입력 순서대로 한다.
#input: logs = ["digi1 8 1 6 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
#output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
# import sys 
# n = sys.stdin.readline()
# m = n
# m = sorted(m[9:-3].split('","'), key=lambda x: x[1])
# print(m)

def reorderLogFiles(self, logs: List[str]) -> List[str]:
    letters, digits = [],[]
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

letters.sort(key=lambda x:(x.split()[1:],x.split()[0]))
re