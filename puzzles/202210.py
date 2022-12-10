from typing import List
from supports import get_input_io


def get_input_list() -> List[List[str]]:
    with get_input_io("202210.txt") as fio:
        input_str_list = fio.readlines()
    result_arr = [x.replace("\n", "").split(" ") for x in input_str_list]
    return result_arr


def main_1():
    command_list = get_input_list()

    X = 1
    cycle_list = [1]

    for comm in command_list:
        if comm[0] == "noop":
            cycle_list.append(X)
        else:
            value = int(comm[1])
            cycle_list.append(X)
            X += value
            cycle_list.append(X)

    result = 0
    for i in range(20, 221, 40):
        result += cycle_list[i - 1] * i

    return result


def main_2():
    command_list = get_input_list()

    X = 1
    cycle_list = [1]

    for comm in command_list:
        if comm[0] == "noop":
            cycle_list.append(X)
        else:
            value = int(comm[1])
            cycle_list.append(X)
            X += value
            cycle_list.append(X)

    result_str = "\n"
    for i in range(1, 241, 40):
        for idx, j in enumerate(range(i, i + 40, 1)):
            spirit_loc = (cycle_list[j - 1], cycle_list[j - 1] + 2)
            if spirit_loc[1] >= (idx + 1) >= spirit_loc[0]:
                result_str += "#"
            else:
                result_str += "."
        result_str += "\n"
    return result_str


def performance():
    main_1()
    main_2()
