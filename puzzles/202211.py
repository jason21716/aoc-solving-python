from typing import List, Callable, Optional
from supports import get_input_io


class Monkey(object):
    def __init__(
        self,
        items: List[int],
        operation: Callable[[int], int],
        test: Callable[[int], bool],
    ) -> None:
        self.initial_items: List[int] = items
        self.items: List[int] = []
        self.operation = operation
        self.test = test
        self.test_true_Monkey: Optional[Monkey] = None
        self.test_false_Monkey: Optional[Monkey] = None
        self.inspected_count: int = 0

    def reset(self):
        self.items = list(self.initial_items)
        self.inspected_count: int = 0

    def receive(self, number: int):
        self.items.append(number)

    def do_thing(self, part_two: bool = False):
        while len(self.items) != 0:
            number = self.items.pop(0)
            if not part_two:
                processed_number = self.operation(number) // 3
            else:
                processed_number = self.operation(number) % 9699690
            if self.test(processed_number):
                self.test_true_Monkey.receive(processed_number)
            else:
                self.test_false_Monkey.receive(processed_number)
            self.inspected_count += 1


monkey_list = [
    Monkey(items=[66, 79], operation=lambda x: x * 11, test=lambda x: ((x % 7) == 0)),
    Monkey(
        items=[84, 94, 94, 81, 98, 75],
        operation=lambda x: x * 17,
        test=lambda x: ((x % 13) == 0),
    ),
    Monkey(
        items=[85, 79, 59, 64, 79, 95, 67],
        operation=lambda x: x + 8,
        test=lambda x: ((x % 5) == 0),
    ),
    Monkey(items=[70], operation=lambda x: x + 3, test=lambda x: ((x % 19) == 0)),
    Monkey(
        items=[57, 69, 78, 78], operation=lambda x: x + 4, test=lambda x: ((x % 2) == 0)
    ),
    Monkey(
        items=[65, 92, 60, 74, 72],
        operation=lambda x: x + 7,
        test=lambda x: ((x % 11) == 0),
    ),
    Monkey(
        items=[77, 91, 91], operation=lambda x: x * x, test=lambda x: ((x % 17) == 0)
    ),
    Monkey(
        items=[76, 58, 57, 55, 67, 77, 54, 99],
        operation=lambda x: x + 6,
        test=lambda x: ((x % 3) == 0),
    ),
]

monkey_list[0].test_true_Monkey = monkey_list[6]
monkey_list[0].test_false_Monkey = monkey_list[7]
monkey_list[1].test_true_Monkey = monkey_list[5]
monkey_list[1].test_false_Monkey = monkey_list[2]
monkey_list[2].test_true_Monkey = monkey_list[4]
monkey_list[2].test_false_Monkey = monkey_list[5]
monkey_list[3].test_true_Monkey = monkey_list[6]
monkey_list[3].test_false_Monkey = monkey_list[0]
monkey_list[4].test_true_Monkey = monkey_list[0]
monkey_list[4].test_false_Monkey = monkey_list[3]
monkey_list[5].test_true_Monkey = monkey_list[3]
monkey_list[5].test_false_Monkey = monkey_list[4]
monkey_list[6].test_true_Monkey = monkey_list[1]
monkey_list[6].test_false_Monkey = monkey_list[7]
monkey_list[7].test_true_Monkey = monkey_list[2]
monkey_list[7].test_false_Monkey = monkey_list[1]


# monkey_list = [
#     Monkey(items=[79, 98], operation=lambda x: x * 19, test=lambda x: ((x % 23) == 0)),
#     Monkey(
#         items=[54, 65, 75, 74],
#         operation=lambda x: x + 6,
#         test=lambda x: ((x % 19) == 0),
#     ),
#     Monkey(
#         items=[79, 60, 97],
#         operation=lambda x: x * x,
#         test=lambda x: ((x % 13) == 0),
#     ),
#     Monkey(items=[74], operation=lambda x: x + 3, test=lambda x: ((x % 17) == 0)),
# ]

# monkey_list[0].test_true_Monkey = monkey_list[2]
# monkey_list[0].test_false_Monkey = monkey_list[3]
# monkey_list[1].test_true_Monkey = monkey_list[2]
# monkey_list[1].test_false_Monkey = monkey_list[0]
# monkey_list[2].test_true_Monkey = monkey_list[1]
# monkey_list[2].test_false_Monkey = monkey_list[3]
# monkey_list[3].test_true_Monkey = monkey_list[0]
# monkey_list[3].test_false_Monkey = monkey_list[1]


def main_1():
    for monkey in monkey_list:
        monkey.reset()

    for _ in range(20):
        for monkey in monkey_list:
            monkey.do_thing()

    inspected_list = [monkey.inspected_count for monkey in monkey_list]
    inspected_list.sort(reverse=True)
    return inspected_list[0] * inspected_list[1]


def main_2():
    for monkey in monkey_list:
        monkey.reset()

    for _ in range(10000):
        for monkey in monkey_list:
            monkey.do_thing(part_two=True)

    inspected_list = [monkey.inspected_count for monkey in monkey_list]
    inspected_list.sort(reverse=True)
    return inspected_list[0] * inspected_list[1]


def performance():
    main_1()
    main_2()
