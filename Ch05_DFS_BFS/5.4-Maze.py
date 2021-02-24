# 실전 5-4 미로 탈출

from collections import deque

n, m = map(int, input().split())

maze_map = []
for i in range(n):
    x_value = list(input())
    maze_map.append(list(map(int, x_value)))

mapping_queue = deque()
mapping_queue.append((0, 0))

# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while mapping_queue:
    y, x = mapping_queue.popleft()
    print(y, x)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 미로를 넘어가면 무시
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue

        # 괴물이면 무시
        if maze_map[ny][nx] == 0:
            continue

        if maze_map[ny][nx] == 1:
            maze_map[ny][nx] = maze_map[y][x] + 1
            mapping_queue.append((ny, nx))

print(maze_map[n - 1][m - 1])
