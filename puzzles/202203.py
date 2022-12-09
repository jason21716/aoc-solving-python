from typing import List
from supports import get_input_io


def get_input_list() -> List[str]:
    with get_input_io("202203.txt") as fio:
        input_str_list = fio.readlines()

    return [x.replace("\n", "") for x in input_str_list]


def same_word(*str_list: str):
    for letter in str_list[0]:
        same_flag = True
        for i in range(1, len(str_list)):
            if letter not in str_list[i]:
                same_flag = False
                break
        if same_flag:
            return letter


def main_1():
    input_obj_list = get_input_list()

    total_score = 0
    for orginal_str in input_obj_list:
        length_orginal_str = len(orginal_str)
        mid_orginal_str = length_orginal_str // 2
        split_str = [
            orginal_str[:mid_orginal_str],
            orginal_str[mid_orginal_str:],
        ]
        same_letter = same_word(*split_str)
        ascii_same_letter = ord(same_letter)
        if ascii_same_letter >= 97:
            ascii_same_letter -= 96
        else:
            ascii_same_letter -= 38
        total_score += ascii_same_letter

    return total_score


def main_2():
    input_obj_list = get_input_list()

    total_score = 0
    for i in range(0, len(input_obj_list), 3):
        str_group = input_obj_list[i : i + 3]
        same_letter = same_word(*str_group)
        ascii_same_letter = ord(same_letter)
        if ascii_same_letter >= 97:
            ascii_same_letter -= 96
        else:
            ascii_same_letter -= 38
        total_score += ascii_same_letter

    return total_score


def performance():
    main_1()
    main_2()
