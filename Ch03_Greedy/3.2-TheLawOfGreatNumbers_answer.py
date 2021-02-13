# 큰 수의 법칙
# M은 더할 횟수
# K는 연속해서 최대로 더할 수 있는 횟수
# 숫자는 같아도 인덱스가 다르면 다른 숫자로 봄
# N은 배열의 크기

# n, m, k 입력받기
n, m, k = map(int, input().split())
# 배열 입력 받기
sample_list = list(map(int, input().split()))

# 가장 큰수 구하기
largest_num = 0
the_second_largest_num = 0
for num in sample_list:
    if num > largest_num:
        the_second_largest_num = largest_num
        largest_num = num
    else:
        if num > the_second_largest_num:
            the_second_largest_num = num

# 가장 큰 수가 곱해지는 횟수 계산
# for 문으로 구하는 것이 아닌 나누기와 나머지를 통해서 미리 계산
a, b = divmod(m, k+1)
count = a * k + b

print(count)
result = largest_num * count + the_second_largest_num * (m-count)
print(result)