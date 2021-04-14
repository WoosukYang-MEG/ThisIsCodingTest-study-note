# 챕터 13.15 특정 거리의 도시 찾기
from collections import deque


def main(k, x):
    queue = deque()
    queue.append(x)
    visited[1] = 0

    result = []
    step = 1
    while queue or step <= k:

        v = queue.popleft()
        for city in graph[v]:  # [2,3]
            visited[city] = min(visited[v] + 1, visited[city])
            queue.append(city)
            if (step == k) and (visited[city] == k):
                result.append(city)

        step += 1

    return result


# 인풋
n, m, k, x = map(int, input().split())

# 도시그래프 from -> to
graph = {}
for i in range(1, n + 1):
    graph[i] = []

# 방문여부
visited = [999999999 for i in range(n + 1)]

# 그래프에 내용 추가
for i in range(m):
    _from, _to = map(int, input().split())
    graph[_from].append(_to)

result = main(k, x)
if result:
    for i in result:
        print(i)
else:
    print(-1)
