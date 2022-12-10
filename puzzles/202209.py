from typing import List, Set, Tuple
from supports import get_input_io


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __eq__(self, that):
        if not isinstance(that, Point):
            return False
        return self.x == that.x and self.y == that.y

    def __hash__(self):
        return 15269 * (15269 + self.x) + self.y

    def __str__(self):
        return f"({self.x}, {self.y})"


def get_input_list() -> List[Tuple[str, int]]:
    with get_input_io("202209.txt") as fio:
        input_str_list = fio.readlines()
    result_arr = [x.replace("\n", "").split(" ") for x in input_str_list]
    result_arr = [(x, int(y)) for x, y in result_arr]
    return result_arr


def debug(h_point: Point, t_point_list: List[Point]):
    print(h_point, end=" ")
    for i in range(9):
        print(t_point_list[i], end=" ")
    print()


def moving(h: Point, t: Point, direction: str) -> Tuple[Point, Point]:
    h_x = h.x
    h_y = h.y
    if direction == "U":
        h_x += 1
    elif direction == "D":
        h_x -= 1
    elif direction == "L":
        h_y -= 1
    elif direction == "R":
        h_y += 1
    target_h = Point(h_x, h_y)

    t_x = t.x
    t_y = t.y

    diff_x = t_x - target_h.x
    diff_y = t_y - target_h.y

    if (
        (diff_x == 0 and diff_y == 0)
        or (abs(diff_x) == 1 and abs(diff_y) == 1)
        or (diff_x == 0 and abs(diff_y) == 1)
        or (abs(diff_x) == 1 and diff_y == 0)
    ):
        pass
    elif diff_x == 0 and abs(diff_y) >= 2:
        t_y = (target_h.y) + (1 if diff_y >= 2 else -1)
    elif abs(diff_x) >= 2 and diff_y == 0:
        t_x = (target_h.x) + (1 if diff_x >= 2 else -1)
    elif abs(diff_x) == 1 and abs(diff_y) >= 2:
        t_x = target_h.x
        t_y = (target_h.y) + (1 if diff_y >= 2 else -1)
    elif abs(diff_x) >= 2 and abs(diff_y) == 1:
        t_x = (target_h.x) + (1 if diff_x >= 2 else -1)
        t_y = target_h.y
    elif abs(diff_x) >= 2 and abs(diff_y) >= 2 and abs(diff_x) == abs(diff_y):
        t_x = (target_h.x) + (1 if diff_x >= 2 else -1)
        t_y = (target_h.y) + (1 if diff_y >= 2 else -1)

    target_t = Point(t_x, t_y)

    return (target_h, target_t)


def main_1():
    input_command = get_input_list()

    t_travel_set: Set[Point] = set()
    h_point = Point(0, 0)
    t_point = Point(0, 0)
    for direction, times in input_command:
        for _ in range(times):
            h_point, t_point = moving(h_point, t_point, direction)
            t_travel_set.add(t_point)

    return len(t_travel_set)


def main_2():
    input_command = get_input_list()

    t_travel_set: Set[Point] = set()
    h_point = Point(0, 0)
    t_point_list = [Point(0, 0) for _ in range(9)]
    for direction, times in input_command:
        for _ in range(times):
            h_point, t_point_list[0] = moving(h_point, t_point_list[0], direction)
            for i in range(8):
                start_point, end_point = moving(
                    t_point_list[i], t_point_list[i + 1], ""
                )
                t_point_list[i] = start_point
                t_point_list[i + 1] = end_point
            t_travel_set.add(t_point_list[8])

    return len(t_travel_set)


def performance():
    main_1()
    main_2()
