import pathlib

root_path = pathlib.Path(__file__).parent.parent.resolve()
input_path = root_path / "inputs"


def get_input_io(filename: str, root: pathlib.Path = input_path):
    file_path = root / filename
    if not file_path.exists():
        raise KeyError("filename not existed.")

    return open(file_path, "r")
