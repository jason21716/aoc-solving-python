from typing import List, Tuple


REINDEER_LIST = [
    (22, 8, 165),
    (8, 17, 114),
    (18, 6, 103),
    (25, 6, 145),
    (11, 12, 125),
    (21, 6, 121),
    (18, 3, 50),
    (20, 4, 75),
    (7, 20, 119),
]
LIMIT_SEC = 2503


def distence_after_seconds(
    reindeer_spec: Tuple[int, int, int], limit_seconds: int
) -> int:
    reindeer_speed, reindeer_spirit, reindeer_rest = reindeer_spec

    current_second = 0
    current_distence = 0

    reindeer_circle_second = reindeer_spirit + reindeer_rest
    reindeer_circle_distence = reindeer_speed * reindeer_spirit

    full_circle_times = limit_seconds // reindeer_circle_second
    current_second += full_circle_times * reindeer_circle_second
    current_distence += full_circle_times * reindeer_circle_distence

    remaining_second = limit_seconds - current_second
    if remaining_second >= reindeer_spirit:
        current_distence += reindeer_speed * reindeer_spirit
    else:
        current_distence += reindeer_speed * remaining_second

    return current_distence


def point_after_seconds(
    reindeer_spec_list: List[Tuple[int, int, int]], limit_seconds: int
) -> int:
    reindeer_point: List[int] = [0 for x in reindeer_spec_list]
    reindeer_distence: List[int] = [0 for x in reindeer_spec_list]
    reindeer_is_running: List[bool] = [True for x in reindeer_spec_list]
    reindeer_speed: List[int] = [x[0] for x in reindeer_spec_list]
    reindeer_remain_spirit_second: List[int] = [x[1] for x in reindeer_spec_list]
    reindeer_remain_rest_second: List[int] = [x[2] for x in reindeer_spec_list]

    for time in range(1, limit_seconds + 1):
        for i in range(len(reindeer_spec_list)):
            if reindeer_is_running[i]:
                reindeer_distence[i] += reindeer_speed[i]
                reindeer_remain_spirit_second[i] -= 1
            else:
                reindeer_remain_rest_second[i] -= 1

            if reindeer_remain_spirit_second[i] == 0:
                reindeer_is_running[i] = False
                reindeer_remain_spirit_second[i] = reindeer_spec_list[i][1]
            elif reindeer_remain_rest_second[i] == 0:
                reindeer_is_running[i] = True
                reindeer_remain_rest_second[i] = reindeer_spec_list[i][2]

        winner_reindeer = -1
        winner_reindeer_distence = -1

        for i in range(len(reindeer_spec_list)):
            if reindeer_distence[i] > winner_reindeer_distence:
                winner_reindeer = i
                winner_reindeer_distence = reindeer_distence[i]
        reindeer_point[winner_reindeer] += 1

    max_point_reindeer_point = -1

    for i in range(len(reindeer_spec_list)):
        if reindeer_point[i] > max_point_reindeer_point:
            max_point_reindeer_point = reindeer_point[i]

    return max_point_reindeer_point


def main_1():
    max_distence = 0
    for reindeer in REINDEER_LIST:
        distence = distence_after_seconds(reindeer, LIMIT_SEC)
        if distence > max_distence:
            max_distence = distence
    return max_distence


def main_2():
    max_point = point_after_seconds(REINDEER_LIST, LIMIT_SEC)
    return max_point


def performance():
    main_1()
    main_2()
