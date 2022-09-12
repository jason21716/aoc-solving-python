from typing import Dict

input_arr = [43, 3, 4, 10, 21, 44, 4, 6, 47, 41, 34, 17, 17, 44, 36, 31, 46, 9, 27, 38]
target_total = 150


class AnswerDict(object):
    def __init__(self):
        self.store: Dict[int, int] = {}

    def add_answer(self, size: int):
        if size not in self.store.keys():
            self.store[size] = 1
        else:
            self.store[size] += 1

    def get_max_size(self):
        min_size = 2147483647
        min_size_count = 0
        for k, v in self.store.items():
            if k < min_size:
                min_size = k
                min_size_count = v
        return min_size_count


def recursive_possible_count(
    current_total: int, current_size: int, current_point: int, answer_dict: AnswerDict
) -> int:
    current_count = 0
    current_size = current_size
    if current_point >= len(input_arr):
        return 0
    for i in range(current_point, len(input_arr)):
        point_value = input_arr[i]
        temp_total = current_total + point_value
        temp_size = current_size + 1
        if temp_total == target_total:
            current_count += 1
            answer_dict.add_answer(temp_size)
        elif temp_total > target_total:
            continue
        else:
            current_count += recursive_possible_count(
                temp_total, temp_size, i + 1, answer_dict
            )
    return current_count

def main():
    answer_dict = AnswerDict()
    total_count = recursive_possible_count(0, 0, 0, answer_dict)
    return total_count, answer_dict

def main_1():
    _, total_count = main()
    return total_count


def main_2():
    answer_dict, _ = main()
    return answer_dict.get_max_size()


def performance():
    main()
