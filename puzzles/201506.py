import re
from typing import List
from supports import get_input_io


def get_input_list() -> List[re.Match]:
    with get_input_io("201506.txt") as fio:
        input_str_list = fio.readlines()
    result_list = []
    for input_str in input_str_list:
        split_command = re.match(
            r"(?P<COMMAND>turn on|turn off|toggle) (?P<S_X>\d*),(?P<S_Y>\d*) through (?P<E_X>\d*),(?P<E_Y>\d*)",
            input_str,
        )
        result_list.append(split_command)
    return result_list


def main_1():
    command_list = get_input_list()
    matrix = [[False for _ in range(1000)] for _ in range(1000)]

    for command in command_list:
        action = command.group("COMMAND")
        s_x = int(command.group("S_X"))
        s_y = int(command.group("S_Y"))
        e_x = int(command.group("E_X"))
        e_y = int(command.group("E_Y"))

        if action == "turn on":
            for x in range(s_x, e_x + 1):
                for y in range(s_y, e_y + 1):
                    matrix[x][y] = True
        elif action == "turn off":
            for x in range(s_x, e_x + 1):
                for y in range(s_y, e_y + 1):
                    matrix[x][y] = False
        elif action == "toggle":
            for x in range(s_x, e_x + 1):
                for y in range(s_y, e_y + 1):
                    matrix[x][y] = not matrix[x][y]

    lit_count = 0
    for x in range(1000):
        for y in range(1000):
            if matrix[x][y]:
                lit_count += 1

    return lit_count


def main_2():
    command_list = get_input_list()
    matrix = [[0 for _ in range(1000)] for _ in range(1000)]

    for command in command_list:
        action = command.group("COMMAND")
        s_x = int(command.group("S_X"))
        s_y = int(command.group("S_Y"))
        e_x = int(command.group("E_X"))
        e_y = int(command.group("E_Y"))

        if action == "turn on":
            for x in range(s_x, e_x + 1):
                for y in range(s_y, e_y + 1):
                    matrix[x][y] += 1
        elif action == "turn off":
            for x in range(s_x, e_x + 1):
                for y in range(s_y, e_y + 1):
                    matrix[x][y] = 0 if matrix[x][y] == 0 else matrix[x][y] - 1
        elif action == "toggle":
            for x in range(s_x, e_x + 1):
                for y in range(s_y, e_y + 1):
                    matrix[x][y] += 2

    lit_count = 0
    for x in range(1000):
        for y in range(1000):
            lit_count += matrix[x][y]

    return lit_count


def performance():
    main_1()
    main_2()
