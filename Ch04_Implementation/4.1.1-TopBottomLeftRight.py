# 예제 4-1 상하좌우
space = int(input())

planner = input().split()

start_point = [1, 1]
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
print(my_position)
