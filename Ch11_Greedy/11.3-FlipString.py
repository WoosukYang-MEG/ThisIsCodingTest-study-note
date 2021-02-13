# 11.3 문자열 뒤집기

s = input()

zero_group = 0
one_group = 0

flag = None
for i in s:
    if flag is None:
        if i == "0":
            flag = "Zero"
            zero_group += 1
        else:
            flag = "One"
            one_group += 1
        continue

    else:
        if flag == "Zero":
            if i == "1":
                flag = "One"
                one_group += 1

        elif flag == "One":
            if i == "0":
                flag = "Zero"
                zero_group += 1

print(min([zero_group, one_group]))
