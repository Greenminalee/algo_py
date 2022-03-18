# N x M 
# k종류의 바이러스
# 1초마다 상하좌우로 증식 번호가 낮은 종류 부터 증식

# S초 뒤에 (X,Y)에 존재하는 바이러스의 종류

# n, k = map(int, input().split())

# graph = []
# for i in range(n):
#     graph.append(list(map(int, input().split())))

# s, x, y = map(int, input().split())


from collections import deque
 
N, K = map(int, input().split())
graph = []
virus = []
for i in range(N):
  graph.append(list(map(int, input().split())))
  for j in range(N):
    if graph[i][j] != 0:
      virus.append(((graph[i][j], i, j)))

print(virus)
S, X, Y = map(int, input().split())


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
 
def bfs(s, X, Y):
  q = deque(virus)
  count = 0
  while q:
    if count == s:
      break
    for _ in range(len(q)):
      prev, x, y = q.popleft()
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
          if graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y]
            q.append((graph[nx][ny], nx, ny))
    count += 1
  return graph[X-1][Y-1]
 
virus.sort()
print(bfs(S, X, Y))
