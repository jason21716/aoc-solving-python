from typing import List
from supports import get_input_io

MATCH_1_RESULT = {
    "X": {"X": 1 + 3, "Y": 2 + 6, "Z": 3 + 0},
    "Y": {"X": 1 + 0, "Y": 2 + 3, "Z": 3 + 6},
    "Z": {"X": 1 + 6, "Y": 2 + 0, "Z": 3 + 3},
}

MATCH_2_RESULT = {
    "X": {"X": 3 + 0, "Y": 1 + 3, "Z": 2 + 6},
    "Y": {"X": 1 + 0, "Y": 2 + 3, "Z": 3 + 6},
    "Z": {"X": 2 + 0, "Y": 3 + 3, "Z": 1 + 6},
}


def get_input_list() -> List[List[str]]:
    with get_input_io("202202.txt") as fio:
        input_str_list = fio.readlines()
    input_obj_list = [
        x.replace("\n", "")
        .replace("A", "X")
        .replace("B", "Y")
        .replace("C", "Z")
        .split(" ")
        for x in input_str_list
    ]
    return input_obj_list


def main_1():
    input_obj_list = get_input_list()
    total_point = 0
    for a, b in input_obj_list:
        total_point += MATCH_1_RESULT[a][b]

    return total_point


def main_2():
    input_obj_list = get_input_list()
    total_point = 0
    for a, b in input_obj_list:
        total_point += MATCH_2_RESULT[a][b]

    return total_point


def performance():
    main_1()
    main_2()
