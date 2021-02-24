# 실전 5-3 음료수 얼려먹기

from collections import deque

ice_frame = []
visited = []

n, m = map(int, input().split())

for i in range(n):
    x_value = list(input())
    ice_frame.append(list(map(int, x_value)))
    visited.append([False] * m)


ice_cream_count = 0
# 모든 부분을 훑을 거임
for y in range(len(ice_frame)):
    for x in range(len(ice_frame[y])):
        value = ice_frame[y][x]
        # 해당 value가 0이고 방문을 안했다면
        if (value == 0) and (visited[y][x] is False):
            # 아이크스림 Queue 생성
            ice_cream_queue = deque()
            ice_cream_queue.append([y, x])
            visited[y][x] = True

            print(f"my {ice_cream_count}번째 아이스크림")
            while ice_cream_queue:

                v = ice_cream_queue.popleft()
                print(v, end=' ')
                new_x, new_y = v[1], v[0]

                # 상하좌우 좌표
                dy = [new_y - 1, new_y + 1, new_y, new_y]
                dx = [new_x, new_x, new_x - 1, new_x + 1]

                # 상하좌우를 queue에 삽입
                for dx_i, dy_i in zip(dx, dy):
                    if (0 <= dx_i <= m-1) and (0 <= dy_i <= n-1):
                        if (ice_frame[dy_i][dx_i] == 0) and (visited[dy_i][dx_i] is False):
                            ice_cream_queue.append([dy_i, dx_i])
                            visited[dy_i][dx_i] = True
            print("")
            ice_cream_count += 1
print(f"ice_cream_count : {ice_cream_count}")