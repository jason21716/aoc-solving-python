import copy
from typing import List
from supports import get_input_io


def get_input_str() -> str:
    with get_input_io("202206.txt") as fio:
        input_str = fio.read()
    return input_str


def unique_letter_substring_end_index(input_str: str, unique_letter_count: int):
    for idx in range(len(input_str) - unique_letter_count):
        sub_str = input_str[idx : idx + unique_letter_count]
        singal_set = set()
        for letter in sub_str:
            singal_set.add(letter)
        if len(singal_set) == unique_letter_count:
            return idx + unique_letter_count


def main_1():
    input_str = get_input_str()

    return unique_letter_substring_end_index(input_str, 4)


def main_2():
    input_str = get_input_str()

    return unique_letter_substring_end_index(input_str, 14)


def performance():
    main_1()
    main_2()
