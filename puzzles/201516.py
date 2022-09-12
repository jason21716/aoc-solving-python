import re
from typing import List, Tuple
from collections import namedtuple

from supports import get_input_io

FILTER = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

Record = namedtuple(
    "Record",
    [
        "id",
        "obj1_name",
        "obj1_count",
        "obj2_name",
        "obj2_count",
        "obj3_name",
        "obj3_count",
    ],
)


def get_input_list() -> List[Record]:
    with get_input_io("201516.txt") as fio:
        input_str = fio.read()

    result_match = re.findall(
        r"Sue (?P<id>\d*): (?P<obj1_name>\w*): (?P<obj1_count>\d*), (?P<obj2_name>\w*): (?P<obj2_count>\d*), (?P<obj3_name>\w*): (?P<obj3_count>\d*)",
        input_str,
    )
    result_list = []

    for (
        id,
        obj1_name,
        obj1_count,
        obj2_name,
        obj2_count,
        obj3_name,
        obj3_count,
    ) in result_match:
        result_list.append(
            Record(
                id,
                obj1_name,
                int(obj1_count),
                obj2_name,
                int(obj2_count),
                obj3_name,
                int(obj3_count),
            )
        )

    return result_list


def main_1():
    records = get_input_list()
    match_list = []
    for record in records:
        filter_tags = [False, False, False]
        obj_names = [record.obj1_name, record.obj2_name, record.obj3_name]
        obj_counts = [record.obj1_count, record.obj2_count, record.obj3_count]
        for i in range(3):
            if obj_names[i] in FILTER.keys():
                if obj_counts[i] == FILTER[obj_names[i]]:
                    filter_tags[i] = True

        if filter_tags[0] and filter_tags[1] and filter_tags[2]:
            match_list.append(record.id)
    return ",".join(match_list)


def main_2():
    records = get_input_list()
    match_list = []
    for record in records:
        filter_tags = [False, False, False]
        obj_names = [record.obj1_name, record.obj2_name, record.obj3_name]
        obj_counts = [record.obj1_count, record.obj2_count, record.obj3_count]
        for i in range(3):
            if obj_names[i] in FILTER.keys():
                if (
                    (
                        obj_counts[i] > FILTER[obj_names[i]]
                        and obj_names[i] in ["cats", "trees"]
                    )
                    or (
                        obj_counts[i] < FILTER[obj_names[i]]
                        and obj_names[i] in ["pomeranians", "goldfish"]
                    )
                    or (
                        obj_counts[i] == FILTER[obj_names[i]]
                        and obj_names[i]
                        not in ["cats", "trees", "pomeranians", "goldfish"]
                    )
                ):
                    filter_tags[i] = True

        if filter_tags[0] and filter_tags[1] and filter_tags[2]:
            match_list.append(record.id)
    return ",".join(match_list)


def performance():
    main_1()
    main_2()
