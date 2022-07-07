#BOJ 11403
#경로 찾기

'''
가중치 없는 방향 그래프 G가 주어졌을 때, 모든 정점 (i, j)에 대해서, 
i에서 j로 가는 경로가 있는지 없는지 구하는 프로그램을 작성하시오.'''

'''
첫째 줄에 정점의 개수 N (1 ≤ N ≤ 100)이 주어진다. 
둘째 줄부터 N개 줄에는 그래프의 인접 행렬이 주어진다. 
i번째 줄의 j번째 숫자가 1인 경우에는 i에서 j로 가는 간선이 존재한다는 뜻이고, 0인 경우는 없다는 뜻이다. 
i번째 줄의 i번째 숫자는 항상 0이다.'''

#인접행렬 -> dfs -> 1이면 계속 돌기 / 0이면 skip 

'''
i 012
j
0  010
1  001
2  100
'''

# dfs
# import sys
# n = int(sys.stdin.readline())


#참고한 풀이
n = int(input())
visit = [0 for i in range(n)]
graph = []
def dfs(v):
    for i in range(n):
        if visit[i] == 0 and graph[v][i] == 1:
            visit[i] = 1
            dfs(i)
for i in range(n):
    graph.append(list(map(int, input().split())))
for i in range(n):
    dfs(i)
    for j in range(n):
        if visit[j] == 1:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
    visit = [0 for i in range(n)]

#플로이드 ?? 알고리즘에 대해 공부
'''
다익스트라 알고리즘은 한 시작점에서 다른 정점까지의 최단 거리를 구하는데 반해 
플로이드 알고리즘은 모든 정점 쌍에 대해서 둘 사이의 최단 거리를 구할 수 있습니다!
단, 플로이드 알고리즘은 음수 가중치가 없는 무조건 양수의 그래프에서 동작합니다.

플로이드-워셜 알고리즘은 시간 복잡도가 O(n^3)으로, 
그래프의 크기가 작아 세제곱 시간 알고리즘을 적용해도 문제가 풀릴 때만 사용할 수 있습니다.'''