from typing import List
from supports import get_input_io


def get_input_str() -> List[str]:
    with get_input_io("202201.txt") as fio:
        input_str_list = fio.readlines()
    return input_str_list


def main_1():
    result_list = []
    current_cal = 0
    for input in get_input_str():
        if input == "\n":
            result_list.append(current_cal)
            current_cal = 0
        else:
            input_cal = int(input.removesuffix("\n"))
            current_cal += input_cal
    return max(result_list)


def main_2():
    result_list = []
    current_cal = 0
    for input in get_input_str():
        if input == "\n":
            result_list.append(current_cal)
            current_cal = 0
        else:
            input_cal = int(input.removesuffix("\n"))
            current_cal += input_cal
    result_list_sorted = sorted(result_list, reverse=True)
    result_cal = result_list_sorted[0] + result_list_sorted[1] + result_list_sorted[2]
    return result_cal


def performance():
    main_1()
    main_2()
