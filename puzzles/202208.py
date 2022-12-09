from typing import List
from supports import get_input_io


def get_input_list() -> List[List[int]]:
    with get_input_io("202208.txt") as fio:
        input_str_list = fio.readlines()

    return [[int(letter) for letter in x.replace("\n", "")] for x in input_str_list]


def debug(array: List[List[bool]]):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(1 if array[i][j] else 0, end="")
        print()
    print("-" * len(array))


def main_1():
    map = get_input_list()
    map_x_length = len(map)
    map_y_length = len(map[0])

    visiable_map = [[False for _ in range(map_y_length)] for _ in range(map_x_length)]

    # Left to Right
    for i in range(map_x_length):
        current_vis_height = -1
        for j in range(map_y_length):
            current_height = map[i][j]
            if current_height > current_vis_height:
                visiable_map[i][j] = True
                current_vis_height = current_height

    # Right to Left
    for i in range(map_x_length - 1, -1, -1):
        current_vis_height = -1
        for j in range(map_y_length - 1, -1, -1):
            current_height = map[i][j]
            if current_height > current_vis_height:
                visiable_map[i][j] = True
                current_vis_height = current_height

    # Up to Down
    for i in range(map_y_length):
        current_vis_height = -1
        for j in range(map_x_length):
            current_height = map[j][i]
            if current_height > current_vis_height:
                visiable_map[j][i] = True
                current_vis_height = current_height

    # Down to Up
    for i in range(map_y_length - 1, -1, -1):
        current_vis_height = -1
        for j in range(map_x_length - 1, -1, -1):
            current_height = map[j][i]
            if current_height > current_vis_height:
                visiable_map[j][i] = True
                current_vis_height = current_height

    # Calculate
    total_count = 0
    for i in range(map_x_length):
        for j in range(map_y_length):
            total_count += 1 if visiable_map[i][j] else 0

    return total_count


def main_2():
    map = get_input_list()
    map_x_length = len(map)
    map_y_length = len(map[0])

    highest_view_score = 0
    for i in range(1, map_x_length - 1, 1):
        for j in range(1, map_y_length - 1, 1):
            current_height = map[i][j]
            current_view_score: int = 1
            # To Right
            direction_view_score = 0
            for j2 in range(j + 1, map_y_length, 1):
                direction_view_score += 1
                if map[i][j2] < current_height:
                    pass
                else:
                    break
            current_view_score *= direction_view_score
            # To Left
            direction_view_score = 0
            for j2 in range(j - 1, -1, -1):
                direction_view_score += 1
                if map[i][j2] < current_height:
                    pass
                else:
                    break
            current_view_score *= direction_view_score
            # To Down
            direction_view_score = 0
            for i2 in range(i + 1, map_x_length, 1):
                direction_view_score += 1
                if map[i2][j] < current_height:
                    pass
                else:
                    break
            current_view_score *= direction_view_score
            # To Up
            direction_view_score = 0
            for i2 in range(i - 1, -1, -1):
                direction_view_score += 1
                if map[i2][j] < current_height:
                    pass
                else:
                    break
            current_view_score *= direction_view_score

            if highest_view_score < current_view_score:
                highest_view_score = current_view_score
    return highest_view_score


def performance():
    main_1()
    main_2()
