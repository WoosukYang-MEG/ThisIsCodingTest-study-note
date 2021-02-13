# 숫자 카드 게임

# N은 행, M은 열
n, m = map(int, input().split())
sample_list = []
for i in range(1,n+1):
    sample_list.append(list(map(int, input().split())))

print(sample_list)


biggest_num_in_small_numbers = None
for low_list in sample_list:
    low_list.sort()
    small_number = low_list[0]
    if not biggest_num_in_small_numbers:
        biggest_num_in_small_numbers = small_number
    else:
        if biggest_num_in_small_numbers < small_number:
            biggest_num_in_small_numbers = small_number

print(biggest_num_in_small_numbers)