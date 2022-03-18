from collections import deque

n, m, k, x = map(int, input().split())

# graph = [[0] * (n + 1) for i in range(n + 1)]
# visited = [[0] * (n + 1)]

# for i in range(m):
#     x, y = map(int, input().split())
#     graph[x][y] = 1
#     graph[y][x] = 1


# def dfs(start):
#     visited[start] = 1
#     for i in graph[start]:
#         if (graph[i] == 0):
#             dfs(i)

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n + 1)
distance[x] = 0

q = deque([x])

while q:
    now = q.popleft()

    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

if (check == False):
    print(-1)
