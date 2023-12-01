from typing import Callable
import time


def read_input(day: int) -> list[str]:
    """Reads the input file for a given day and returns a list of lines"""
    with open(f"data/day{day}.txt", "r") as f:
        return f.read().splitlines()


def stop_watch(func: Callable) -> Callable:
    """ Decorator to print the time taken for a function to run"""
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        time_taken = (time.time() - start) * 1000
        print(f"Time taken: {time_taken:.2f} ms")
    return wrapper
