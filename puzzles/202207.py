from typing import List, Dict
from supports import get_input_io
import re


def get_input_list() -> List[List[str]]:
    with get_input_io("202207.txt") as fio:
        input_str_list = fio.readlines()

    return [x.replace("\n", "").split(" ") for x in input_str_list]


class File:
    def __init__(self, size: int, name: str) -> None:
        self.size: int = size
        self.name: str = name


class Node:
    def __init__(self, parent: "Node") -> None:
        self.sub_folder_dict: Dict[str, "Node"] = {}
        self.file_list: List[File] = []
        self.parent: Node = parent

    def get_folder_size(self) -> int:
        total_size: int = 0
        for file in self.file_list:
            total_size += file.size
        for _, folder_node in self.sub_folder_dict.items():
            total_size += folder_node.get_folder_size()
        return total_size

    def add_file(self, size: int, name: str):
        new_file = File(size, name)
        self.file_list.append(new_file)

    def add_folder(self, name: str):
        self.sub_folder_dict[name] = Node(self)

    def get_sub_folder(self, name: str):
        return self.sub_folder_dict[name]

    def get_parent(self):
        return self.parent


def create_file_structure(command_list_list: List[List[str]]):
    file_tree_root = Node(None)

    pointer: Node = file_tree_root

    for command_list in command_list_list:
        if command_list[0] == "$":
            if command_list[1] == "cd":
                if command_list[2] == "/":
                    pointer = file_tree_root
                elif command_list[2] == "..":
                    pointer = pointer.get_parent()
                else:
                    pointer = pointer.get_sub_folder(command_list[2])
            elif command_list[1] == "ls":
                pass
        elif command_list[0] == "dir":
            pointer.add_folder(command_list[1])
        else:
            size_int = int(command_list[0])
            pointer.add_file(size_int, command_list[1])
    return file_tree_root


def main_1_recursive(current_node: Node):
    temp_total: int = 0
    for _, folder_node in current_node.sub_folder_dict.items():
        temp_total += main_1_recursive(folder_node)
    if current_node.get_folder_size() < 100000:
        temp_total += current_node.get_folder_size()
    return temp_total


def main_2_recursive(current_node: Node, limit_size: int):
    temp_total: int = 10000000000
    for _, folder_node in current_node.sub_folder_dict.items():
        sub_folder_target = main_2_recursive(folder_node, limit_size)
        if temp_total > sub_folder_target > limit_size:
            temp_total = sub_folder_target
    current_node_size = current_node.get_folder_size()
    if temp_total > current_node_size > limit_size:
        temp_total = current_node_size
    return temp_total


def main_1():
    input_obj_list = get_input_list()
    document_root = create_file_structure(input_obj_list)

    return main_1_recursive(document_root)


def main_2():
    input_obj_list = get_input_list()
    document_root = create_file_structure(input_obj_list)

    current_free_size = 70000000 - document_root.get_folder_size()
    need_free_size = 30000000 - current_free_size

    return main_2_recursive(document_root, need_free_size)


def performance():
    main_1()
    main_2()
