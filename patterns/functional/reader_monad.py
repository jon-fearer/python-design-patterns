from typing import Callable


def unit(input_val: str) -> str:
    return input_val


def bind(reader: Callable, transform: Callable):
    return None
