# 예제 4-1.1 상하좌우

# n 입력
space = int(input())

# planner 입력
planner = input().split()

# 시작포인트 설정
start_point = [1, 1]

# 문자에 따르 조건확인후 이동
my_position = start_point
for i in planner:
    if i == "L" and my_position[1] != 1:
        my_position[1] -= 1
    elif i == "R" and my_position[1] != space:
        my_position[1] += 1
    elif i == "U" and my_position[0] != 1:
        my_position[0] -= 1
    elif i == "D" and my_position[0] != space:
        my_position[0] += 1
#결과 출력
print(my_position)
