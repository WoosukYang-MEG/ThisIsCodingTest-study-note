# 8.3 개미전사

n = int(input())

ware_house = list(map(int, input().split()))

dp_table = [0] * len(ware_house)

dp_table[0] = ware_house[0]
dp_table[1] = max(ware_house[0], ware_house[1])

for i in range(2, n):
    dp_table[i] = max(dp_table[i-1], dp_table[i-2] + ware_house[i])

print(dp_table[-1])
