# 실전 4-3 게임 개발 문제

class MyPosition:
    def __init__(self, y, x, direction, column, row):
        self.pos_y = y
        self.pos_x = x
        self.direction = direction
        self.direction_way = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북 동 남 서
        self.direction_way_korean = ["북", "동", "남", "서"]
        self.watching_way = [(0, -1), (-1, 0), (0, 1), (1, 0)]  # 서 북 동 남
        self.column = column
        self.row = row
        self.my_map = self.making_my_map()

    def making_my_map(self):
        my_map = []
        for k in range(self.row):
            my_map.append([0] * self.column)
        my_map[self.pos_y][self.pos_x] = 2
        return my_map

    def rotate_counter_clockwise(self):
        self.direction -= 1
        if self.direction == -1:
            self.direction = 3

    def search_for_left_location(self):
        y = self.pos_y + self.watching_way[self.direction][0]
        x = self.pos_x + self.watching_way[self.direction][1]
        return y, x

    def did_you_search_for_surrounds(self):
        steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for step in steps:
            y = self.pos_y + step[0]
            x = self.pos_x + step[1]
            if (0 <= y <= self.row) and (0 <= x <= self.column):
                if self.my_map[y][x] == 0:
                    return False
        return True


column, row = map(int, input().split())
pos_y, pos_x, direction = map(int, input().split())

my_character = MyPosition(pos_y, pos_x, direction, column, row)

game_map = []
for i in range(row):
    game_map.append(list(map(int, input().split())))

count = 1
while True:
    print("------------------------------------------------")
    print(f"현재 위치 : {my_character.pos_y, my_character.pos_x}")
    print(f"내가 보는 방향 : {my_character.direction_way_korean[my_character.direction]}")
    for i in range(4):
        print(my_character.my_map[i])

    # 4방향 전부 가본곳인지 확인
    if my_character.did_you_search_for_surrounds() is True:
        next_y = my_character.pos_y + my_character.direction_way[direction][0]
        next_x = my_character.pos_x + my_character.direction_way[direction][1]
        if game_map[next_y][next_x] == 1:
            break
        else:
            my_character.pos_y = next_y
            my_character.pos_x = next_x

    else:
        # 바라보는 방향 기준 왼쪽 지형 index 탐색
        watching_pos_y, watching_pos_x = my_character.search_for_left_location()
        print(f"바라보는 위치 : {watching_pos_y, watching_pos_x}")
        # 해당 index 가 맵을 벗어나는지 확인
        if (0 <= watching_pos_y <= row) and (0 <= watching_pos_x <= column):
            # 가보지 않은 지형이
            if my_character.my_map[watching_pos_y][watching_pos_x] == 0:
                # 바다라면 처음부터 다시
                if game_map[watching_pos_y][watching_pos_x] == 1:
                    my_character.my_map[watching_pos_y][watching_pos_x] = 1
                    my_character.rotate_counter_clockwise()
                # 땅이라면 내위치를 보는 방향으로 이동 & 보는 방향 갱신
                else:
                    my_character.rotate_counter_clockwise()
                    my_character.pos_y = watching_pos_y
                    my_character.pos_x = watching_pos_x
                    my_character.my_map[watching_pos_y][watching_pos_x] = 2
                    count += 1
            # 가본 지형이라면 왼쪽으로 회전
            else:
                my_character.rotate_counter_clockwise()
        # 맵을 벗어난다면 회전
        else:
            my_character.rotate_counter_clockwise()

print(count)
