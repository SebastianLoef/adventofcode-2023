from src.utils import read_input, stop_watch
from math import prod
from collections import defaultdict

def get_color(string: str):
    for i, c in enumerate(string):
        if c.isalpha():
            return c, int(string[:i])


def format_data(data: str) -> list:
    """Converts the input data into a list of tuples"""
    new_data = []
    for i, line in enumerate(data):
        game_str, draws = line.split(":")
        game = []
        for j, draw in enumerate(draws.split(";")):
            draw = draw.strip()
            colors = draw.split(",")
            game.append([get_color(color) for color in colors])
        new_data.append(game)
    return new_data


def is_draw_valid(draw: list, max_num: dict) -> bool:
    """Checks if a draw is valid"""
    for i, (color, count) in enumerate(draw):
        if count > max_num[color]:
            return False
    return True


def is_game_valid(game: list, max_num: dict) -> bool:
    """Checks if a game is valid"""
    for i, draw in enumerate(game):
        if not is_draw_valid(draw, max_num):
            return False
    return True


def part1(data: str) -> int:
    max_num = {"r": 12, "g": 13, "b": 14}
    return sum(i + 1 for i, game in enumerate(data) if is_game_valid(game, max_num))


def min_cubes_game(game: list) -> dict[int]:
    """Returns the minimum number of cubes that can be drawn for a given draw"""
    min_cubes = defaultdict(int)
    for draw in game:
        for i, (color, count) in enumerate(draw):
            min_cubes[color] = max(min_cubes[color], count)
    return min_cubes


def product(d: dict) -> int:
    """Returns the product of all values in a dictionary"""
    return prod(d.values())


def part2(data: str) -> int:
    return sum(product(min_cubes_game(game)) for game in data)

@stop_watch
def main(data: str) -> None:
    data = format_data(data)
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == "__main__":
    data = read_input(2)
    main(data)
