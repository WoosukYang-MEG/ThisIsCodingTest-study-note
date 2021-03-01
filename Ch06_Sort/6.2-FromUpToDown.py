# 실전 6-2 위에서 아래로

n = int(input())

num_list = []
for i in range(n):
    num_list.append(int(input()))

num_list.sort(reverse=True)

for num in num_list:
    print(num, end=" ")
