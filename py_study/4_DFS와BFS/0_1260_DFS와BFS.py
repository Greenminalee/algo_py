# 문제
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 
# 정점 번호는 1번부터 N번까지이다.

# 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 
# 입력으로 주어지는 간선은 양방향이다.

# 출력
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

from collections import deque

N, M, V = map(int, input().split())

graph = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
  m1, m2 = map(int, input().split())
  # 노드 연결 하기
  graph[m1][m2] = graph[m2][m1] = 1

# # 너비 우선 탐색
# def bfs(start_v):
#   discoverd = [start_v]
#   # 리스트를 써서 pop(0)하게 되면 시간복잡도가 O(N)이다.
#   # 그래서 시간복잡도가 O(1)인 deque를 사용한다.
#   queue = deque() 
#   queue.append(start_v)

#   while queue:
#     v = queue.popleft()
#     print(v, end=' ')

#     for w in range(len(graph[start_v])):
#       if graph[v][w] == 1 and (w not in discoverd):
#         discoverd.append(w)
#         queue.append(w)

# # 깊이 우선 탐색
def dfs(start_v, discoverd=[]):
  discoverd.append(start_v)
  print(start_v, end=' ')

  for w in range(len(graph[start_v])):
    if graph[start_v][w] == 1 and (w not in discoverd):
      dfs(w, discoverd)

dfs(V)


# print()
# bfs(V)


# number = [0 for i in range(1, 11)]

# print(number)

# N, M, V = map(int, input().split())

# graph = [[0] * (N + 1) for i in range(N + 1)]

# for i in range(M):
#     y, x = map(int, input().split())
#     graph[y][x] = 1
#     graph[x][y] = 1
# for i in graph:
#     print(i)
