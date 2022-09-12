ROW_NUM = 3010
COL_NUM = 3019
START_CODE = 20151125


def main_1():
    position = (ROW_NUM + COL_NUM) * (ROW_NUM + COL_NUM - 1) // 2 - ROW_NUM + 1

    def next_code(previous_code: int):
        return previous_code * 252533 % 33554393

    current_code = START_CODE
    for i in range(1, position):
        current_code = next_code(current_code)
    return current_code


def main_2():
    return None


def performance():
    main_1()
    main_2()
