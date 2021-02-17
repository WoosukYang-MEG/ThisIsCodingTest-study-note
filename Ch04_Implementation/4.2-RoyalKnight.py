# 실전 4-2 왕실의 나이트 문제

position = input()

x_pos = position[0]
y_pos = int(position[1])

possible_way = 8
if y_pos < 3:
    possible_way -= 2
    if y_pos < 2:
        possible_way -= 1

elif y_pos > 6:
    possible_way -= 2
    if y_pos > 7:
        possible_way -= 1

if x_pos < "c":
    possible_way -= 2
    if x_pos < "b":
        possible_way -= 1

elif x_pos > "f":
    possible_way -= 2
    if x_pos > "g":
        possible_way -= 1


print(possible_way)
