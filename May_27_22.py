#BOJ12605
#단어순서 뒤집기
#64ms

'''스페이스로 띄어쓰기 된 단어들의 리스트가 주어질때, 단어들을 반대 순서로 뒤집어라.
각 라인은 w개의 영단어로 이루어져 있으며, 총 L개의 알파벳을 가진다.
각 행은 알파벳과 스페이스로만 이루어져 있다.
단어 사이에는 하나의 스페이스만 들어간다.'''

#input
# 3
# this is a test
# foobar
# all your base

#output
# Case #1: test a is this
# Case #2: foobar
# Case #3: base your all
# print(f'Case #{}: {}',i+1,바뀐문장)


for i in range(int(input())):
    lst = input().split()
    f_lst = []
    for j in range(len(lst)):
        f_lst.append(lst.pop())
    sentence = " ".join(f_lst)
    print(f'Case #{i+1}: {sentence}')