import pathlib


# todo remove this directory, not in line with oop
def get_base_directory():
    return pathlib.Path(__file__).resolve().parent
