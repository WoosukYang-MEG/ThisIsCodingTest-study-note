# 예제 4-2 시각
import time

n = int(input())

start_time = time.time()
result = 0
for i in range(n + 1):
    if i % 3 == 0 and i > 0:
        result += 60 * 60
    else:
        result += 60 * 15 + 15 * 60 - 15 * 15

print(result)
print(time.time() - start_time)
