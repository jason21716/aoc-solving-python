from typing import List
from supports import get_input_io
import re


def get_input_list() -> List[List[str]]:
    with get_input_io("202204.txt") as fio:
        input_str_list = fio.readlines()

    return [map(int, re.split(r"[,\-]", x.replace("\n", ""))) for x in input_str_list]


def main_1():
    input_obj_list = get_input_list()
    count = 0
    for a_min, a_max, b_min, b_max in input_obj_list:
        flag_a_contain_b = (a_min <= b_min) and (a_max >= b_max)
        flag_b_contain_a = (b_min <= a_min) and (b_max >= a_max)
        if flag_a_contain_b or flag_b_contain_a:
            count += 1
    return count


def main_2():
    input_obj_list = get_input_list()
    count = 0
    for a_min, a_max, b_min, b_max in input_obj_list:
        flag_a_contain_b = (b_min <= a_max and b_min >= a_min) or (
            b_max <= a_max and b_max >= a_min
        )
        flag_b_contain_a = (a_min <= b_max and a_min >= b_min) or (
            a_max <= b_max and a_max >= b_min
        )
        if flag_a_contain_b or flag_b_contain_a:
            count += 1
    return count


def performance():
    main_1()
    main_2()
