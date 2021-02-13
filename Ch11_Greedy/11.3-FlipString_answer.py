# 11.3 문자열 뒤집기

s = input()

zero_group = 0
one_group = 0

if s[0] == "0":
    zero_group += 1
else:
    one_group += 1

for idx, value in enumerate(s[:-1]):
    if value != s[idx+1]:               # 다음 idx와의 비교를 이런식으로 표현
        if s[idx+1] == "0":
            zero_group += 1
        else:
            one_group += 1

print(min(zero_group, one_group))