# 8.4 바닥 공사

n = int(input())

dp_table = [0] * n

dp_table[0] = 1
dp_table[1] = 3

for i in range(2, n):

    dp_table[i] = (dp_table[i-1] + 2 * dp_table[i-2]) % 796796

print(dp_table[-1])
