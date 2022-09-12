from typing import List
from supports import get_input_io


def get_input_list() -> List[List[int]]:
    with get_input_io("201502.txt") as fio:
        input_str_list = fio.readlines()
    input_obj_list = [list(map(int, x.split("x"))) for x in input_str_list]
    return input_obj_list


def main_1():
    input_obj_list = get_input_list()
    total_paper_size = 0
    for input_obj in input_obj_list:
        input_obj.sort()
        total_paper_size += (
            2 * input_obj[0] * input_obj[1]
            + 2 * input_obj[0] * input_obj[2]
            + 2 * input_obj[1] * input_obj[2]
        )
        total_paper_size += input_obj[0] * input_obj[1]
    return total_paper_size


def main_2():
    input_obj_list = get_input_list()
    total_ribbon_size = 0

    for input_obj in input_obj_list:
        input_obj.sort()
        total_ribbon_size += 2 * (input_obj[0] + input_obj[1])
        total_ribbon_size += input_obj[0] * input_obj[1] * input_obj[2]
    return total_ribbon_size


def performance():
    main_1()
    main_2()
