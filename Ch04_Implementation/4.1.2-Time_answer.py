# 예제 4-2 시각 단안예시
import time

h = int(input())

start_time = time.time()
count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):

            if "3" in str(i) + str(j) + str(k):
                count += 1

print(count)
print(time.time() - start_time)
