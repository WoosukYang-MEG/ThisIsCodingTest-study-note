# 8.5 효율적인 화폐 구성

# 화폐종류 n, 타겟 금액 m
n, m = map(int, input().split())

current_list = []
for i in range(n):
    current_list.append(int(input()))

dp_table = [99999] * (m+1)


dp_table[0] = 0
for current in current_list:
    for i in range(current, m+1):
        dp_table[i] = min(dp_table[i], dp_table[i-current] + 1)

    print(dp_table)

if dp_table[-1] != 99999:
    print(dp_table[-1])
else:
    print(-1)