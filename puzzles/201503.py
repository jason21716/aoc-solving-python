from collections import namedtuple
from typing import List
from supports import get_input_io


def get_input_command() -> List[List[str]]:
    with get_input_io("201503.txt") as fio:
        input_str_line = fio.readline()

    input_command_list = [y for y in input_str_line if y != "\n"]
    return input_command_list


Point = namedtuple("Point", ["x", "y"])


def main_1():
    input_command_list = get_input_command()
    visit_location = set()

    current_position_x = 0
    current_position_y = 0
    for command in input_command_list:
        if command == "<":
            current_position_x -= 1
        elif command == ">":
            current_position_x += 1
        elif command == "^":
            current_position_y += 1
        elif command == "v":
            current_position_y -= 1
        else:
            pass
        visit_location.add(Point(current_position_x, current_position_y))

    return len(visit_location)


def main_2():
    input_command_list = get_input_command()
    visit_location = set()

    current_person_position_x = 0
    current_person_position_y = 0
    current_robot_position_x = 0
    current_robot_position_y = 0
    is_person_action = True
    for command in input_command_list:
        if is_person_action:
            if command == "<":
                current_person_position_x -= 1
            elif command == ">":
                current_person_position_x += 1
            elif command == "^":
                current_person_position_y += 1
            elif command == "v":
                current_person_position_y -= 1
            else:
                pass
            visit_location.add(
                Point(current_person_position_x, current_person_position_y)
            )
        else:
            if command == "<":
                current_robot_position_x -= 1
            elif command == ">":
                current_robot_position_x += 1
            elif command == "^":
                current_robot_position_y += 1
            elif command == "v":
                current_robot_position_y -= 1
            else:
                pass
            visit_location.add(
                Point(current_robot_position_x, current_robot_position_y)
            )
        is_person_action = not is_person_action

    return len(visit_location)


def performance():
    main_1()
    main_2()
