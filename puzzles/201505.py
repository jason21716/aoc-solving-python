from typing import List
import re
from supports import get_input_io


def get_input_words() -> List[List[str]]:
    with get_input_io("201505.txt") as fio:
        input_str_list = fio.readlines()

    input_word_list = [x.replace("\n", "") for x in input_str_list]
    return input_word_list


def main_1():
    input_word_list = get_input_words()
    count_nice_words = 0
    for word in input_word_list:
        cond = [False, False, False]

        cond[0] = len(re.findall(r"[aeiou]", word)) >= 3
        cond[1] = len(re.findall(r"(\w)\1", word)) >= 1
        cond[2] = len(re.findall(r"ab|cd|pq|xy", word)) == 0

        cond_result = all(cond)
        if cond_result:
            count_nice_words += 1
    return count_nice_words


def main_2():
    input_word_list = get_input_words()
    count_nice_words = 0
    for word in input_word_list:
        cond = [False, False]

        cond[0] = len(re.findall(r"(\w)\w\1", word)) >= 1
        cond[1] = len(re.findall(r"(\w\w)\w*\1", word)) >= 1

        cond_result = all(cond)
        if cond_result:
            count_nice_words += 1
    return count_nice_words


def performance():
    main_1()
    main_2()
