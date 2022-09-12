from typing import List
from supports import get_input_io

METRIX = [
    [5, -1, 0, 0, 5],
    [-1, 3, 0, 0, 1],
    [0, -1, 4, 0, 6],
    [-1, 0, 0, 2, 8],
]


def main():
    max_score = 0
    max_score_ingredient = None
    cal_500_max_score = 0
    cal_500_max_score_ingredient = None
    for x in range(0, 100 + 1):
        for y in range(0, 100 - x + 1):
            for z in range(0, 100 - x - y + 1):
                w = 100 - x - y - z
                total_score = 1
                for i in range(4):
                    item_score = (
                        METRIX[0][i] * x
                        + METRIX[1][i] * y
                        + METRIX[2][i] * z
                        + METRIX[3][i] * w
                    )
                    total_score *= 0 if item_score <= 0 else item_score
                calories_score = (
                    METRIX[0][4] * x
                    + METRIX[1][4] * y
                    + METRIX[2][4] * z
                    + METRIX[3][4] * w
                )
                if total_score > max_score:
                    max_score = total_score
                    max_score_ingredient = (x, y, z, w)
                if total_score > cal_500_max_score and calories_score == 500:
                    cal_500_max_score = total_score
                    cal_500_max_score_ingredient = (x, y, z, w)
    return (max_score, cal_500_max_score)


def main_1():
    (max_score, _) = main()
    return max_score


def main_2():
    (_, cal_500_max_score) = main()
    return cal_500_max_score


def performance():
    main()
