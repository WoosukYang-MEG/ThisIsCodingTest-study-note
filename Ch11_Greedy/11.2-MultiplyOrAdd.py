# 11.2 곱하기 혹은 더하기

string1 = input()
string_list = list(string1)
string_list = list(map(int, string_list))

result = 0
for n in string_list:
    # result가 0또는1이라면 더하기가 더 큼
    if result in [0, 1]:
        result += n
    else:
        # 추가되는 n이 0또는 1이라면 더하기가 더 큼
        if n in [0, 1]:
            result += n
        # 0,1이외의 숫자라면 곱하기가 더 큼
        else:
            result *= n
print(result)
