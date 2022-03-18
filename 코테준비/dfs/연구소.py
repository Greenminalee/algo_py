# n x m
# 0 1 2
# 안전영역의 크기..


# 벽 만들기 3개
# 바이러스 감염된곳 변경
# 
# 안전구역 판정



# n, m = map(int, input().split())

# graph = [[0] * n for _ in range(m)]

# for i in range(n):
#     graph[i] = list(map(int, input().split()))

# from collections import deque
# import copy

# def bfs():
#     queue = deque()
#     tmp_graph = copy.deepcopy(graph)
#     for i in range(n):
#         for j in range(m):
#             if tmp_graph[i][j] == 2:
#                 queue.append((i, j))

#     while queue:
#         x, y = queue.popleft()

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue
#             if tmp_graph[nx][ny] == 0:
#                 tmp_graph[nx][ny] = 2
#                 queue.append((nx, ny))

#     global answer
#     cnt = 0

#     for i in range(n):
#         cnt += tmp_graph[i].count(0)

#     answer = max(answer, cnt)


# def makeWall(cnt):
#     if cnt == 3:
#         bfs()
#         return

#     for i in range(n):
#         for j in range(m):
#             if graph[i][j] == 0:
#                 graph[i][j] = 1
#                 makeWall(cnt+1)
#                 graph[i][j] = 0

# n, m = map(int, input().split())
# graph = []
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]

# for i in range(n):
#     graph.append(list(map(int, input().split())))

# answer = 0
# makeWall(0)
# print(answer)

n, m = map(int, input().split())
graph = []
temp_graph = [[0] * m for _ in range(n)]

for _ in range():
    graph.append(list(map(int, input().split())))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

result = 0


#깊이 우선 탐색을 이용해 각 바이러스가 퍼질수 있도록
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if (temp_graph[nx][ny] == 0):
                temp_graph[nx][ny] = 2
                virus(nx, ny)
            

# DFS를 이용해 울타리를 설치하면서, 매번 안전 영역의 크기계산
def dfs(count):
    global result

    #울타리가 3개 설치된 경우
    if count == 3:
        #울타리 복사
        for i in range(n):
            for j in range(m):
                if temp_graph[i][j] == 2:
                    virus(i, j)
         #각 바이러스의 위치에서 전파 진행
         for i in range(n):
            for j in range(m):
                if temp_graph[i][j] == 2:
                    

        return
    
    #빈공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                dfs(count)
                graph[i][j] = 0
                count -= 1