from supports import get_input_io


def get_input_str() -> str:
    with get_input_io("201501.txt") as fio:
        input_str = fio.read()
    return input_str


def main_1():
    input_str = get_input_str()
    left_count = input_str.count("(")
    right_count = input_str.count(")")
    return left_count - right_count


def main_2():
    input_str = get_input_str()
    current_level = 0
    current_position = 0
    for letter in input_str:
        current_position += 1
        if letter == "(":
            current_level += 1
        elif letter == ")":
            current_level -= 1
        if current_level < 0:
            break
    return current_position


def performance():
    main_1()
    main_2()
