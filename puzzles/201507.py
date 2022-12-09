import re
from typing import Any, List, Optional
from supports import get_input_io


def get_input_list() -> List[re.Match]:
    with get_input_io("201507.txt") as fio:
        input_str_list = fio.readlines()
    result_list = []
    for input_str in input_str_list:
        split_command = re.match(
            r"(?:(?:(?P<SOURCE_B>\w*) )?(?P<OPERATOR>\w*) )?(?P<SOURCE_A>\w*) -> (?P<TARGET>\w*)",
            input_str,
        )
        result_list.append(split_command)
    return result_list


def parse_int(s: str, default: Any) -> Optional[int]:
    try:
        return int(s)
    except Exception:
        return default


def main_1():
    wire_dict = {}
    for command_line in get_input_list():
        source_a = parse_int(
            command_line.group("SOURCE_A"), command_line.group("SOURCE_A")
        )
        source_b = parse_int(
            command_line.group("SOURCE_B"), command_line.group("SOURCE_B")
        )
        operator = command_line.group("OPERATOR")
        target = command_line.group("TARGET")


def main_2():
    pass


def performance():
    main_1()
    main_2()
