# 실전 4-2 왕실의 나이트 문제

# 나이트 위치 입력
position = input()
row = int(position[1])
column = int(ord(position[0])) - int(ord("a")) + 1

# 나이트가 이동가능한 8가지 방법
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]


# 나이트 이동가능여부 판단
count = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 이동이 가능하다면 카운트 증가
    if (1 <= next_row <= 8) and (1 <= next_column <= 8):
        count += 1

print(count)