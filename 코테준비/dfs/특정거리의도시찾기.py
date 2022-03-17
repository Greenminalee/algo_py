from collections import deque

n, m, x, k = map(int, input().split())

graph = [[0] * (n + 1) for i in range(n + 1)]
visited = [[0] * (n + 1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1


def dfs(start):
    visited[start] = 1
    for i in graph[start]:
        if 