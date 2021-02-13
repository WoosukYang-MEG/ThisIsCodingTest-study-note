# 큰 수의 법칙
# M은 더할 횟수
# K는 연속해서 최대로 더할 수 있는 횟수
# 숫자는 같아도 인덱스가 다르면 다른 숫자로 봄
# N은 배열의 크기

N, M, K = map(int, input().split())
sample_list = list(map(int, input().split()))

max_int = max(sample_list)

largest_num = 0
the_second_largest_num = 0
for num in sample_list:
    if num > largest_num:
        the_second_largest_num = largest_num
        largest_num = num
    else:
        if num > the_second_largest_num:
            the_second_largest_num = num


result = 0
counter = K
for i in range(1,M+1):
    if counter == 0:
        counter = K
        result += the_second_largest_num

    else:
        result += largest_num
        counter -= 1

print(result)

