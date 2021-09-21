from typing import Callable


def string_processor(input_string: str, operation: Callable[[str], str]) -> None:
    print(operation(input_string), end='')

