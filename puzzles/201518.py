from typing import List
from supports import get_input_io


def get_input_matrix() -> List[List[str]]:
    with get_input_io("201518.txt") as fio:
        input_str_list = fio.readlines()

    input_obj_list = [[y for y in x if y != "\n"] for x in input_str_list]
    return input_obj_list


class LightMatrix:
    def __init__(
        self, input_str_list: List[List[str]], is_four_corner_on: bool = False
    ):
        self._grid = input_str_list
        self.x_range = len(input_str_list)
        self.y_range = len(input_str_list[0])
        self.step = 0
        self.is_four_corner_on = is_four_corner_on
        if self.is_four_corner_on:
            self._light_on_four_corner()

    def _light_on_four_corner(self):
        four_corner = [
            (0, 0),
            (self.x_range - 1, 0),
            (0, self.y_range - 1),
            (self.x_range - 1, self.y_range - 1),
        ]
        for x, y in four_corner:
            self._grid[x][y] = "#"

    def _get_neighbor_count(self, x: int, y: int) -> int:
        neighbor_count = 0
        neighbor_position = [
            (x - 1, y - 1),
            (x - 1, y),
            (x - 1, y + 1),
            (x, y - 1),
            (x, y + 1),
            (x + 1, y - 1),
            (x + 1, y),
            (x + 1, y + 1),
        ]
        for n_x, n_y in neighbor_position:
            if n_x < 0 or n_x >= self.x_range or n_y < 0 or n_y >= self.y_range:
                continue
            if self._grid[n_x][n_y] == "#":
                neighbor_count += 1
        return neighbor_count

    def _get_animate_result(self, current_light: str, neighbor_count: int) -> str:
        if current_light == "#":
            if neighbor_count in [2, 3]:
                return "#"
            else:
                return "."
        else:
            if neighbor_count == 3:
                return "#"
            else:
                return "."

    def run_next_step(self) -> None:
        next_step_grid = [["." for _ in range(100)] for _ in range(100)]
        for x in range(self.x_range):
            for y in range(self.y_range):
                current_light = self._grid[x][y]
                neighbor_count = self._get_neighbor_count(x, y)
                next_step_light = self._get_animate_result(
                    current_light, neighbor_count
                )
                next_step_grid[x][y] = next_step_light
        self._grid = next_step_grid
        if self.is_four_corner_on:
            self._light_on_four_corner()
        self.step += 1

    def run_steps(self, step_count: int) -> None:
        for _ in range(step_count):
            self.run_next_step()

    def get_total_lights_on(self) -> int:
        total_on = 0
        for x in range(self.x_range):
            for y in range(self.y_range):
                if self._grid[x][y] == "#":
                    total_on += 1
        return total_on


def main_1():
    input_obj_list = get_input_matrix()
    matrix = LightMatrix(input_obj_list)
    matrix.run_steps(100)
    return matrix.get_total_lights_on()


def main_2():
    input_obj_list = get_input_matrix()
    matrix = LightMatrix(input_obj_list, is_four_corner_on=True)
    matrix.run_steps(100)
    return matrix.get_total_lights_on()


def performance():
    main_1()
    main_2()
