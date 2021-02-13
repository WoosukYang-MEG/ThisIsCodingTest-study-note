# 11.1 모험가 길드

n = int(input())
sample_list = list(map(int, input().split()))

sample_list.sort(reverse=True)


len_list = len(sample_list)
count = 0
start_idx = 0
start_num = None
while True:
    if len_list > start_idx:
        count += 1

        start_num = sample_list[start_idx]
        start_idx += start_num
    else:
        break

print(count)






