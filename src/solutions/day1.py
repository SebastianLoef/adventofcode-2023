from src.utils import read_input, stop_watch

STR_NUMBERS = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]     

def part1(data: list[str]) -> int:
    summan = 0
    for row in data:
        first_digit = ""
        last_digit = ""
        for i, char in enumerate(row):
            if first_digit and last_digit:
                break
            char_r = row[len(row) - i - 1]
            if not first_digit and char.isnumeric():
                first_digit = char
            if not last_digit and char_r.isnumeric():
                last_digit = char_r
        summan += int(first_digit + last_digit)
    return summan

def find_spelled_out(string: str) -> tuple[int, str, int, str]:
    """Returns the index of the first and last spelled out number of string"""
    min_loc, max_loc = len(string), -1
    min_num, max_num = "", ""
    for i, num in enumerate(STR_NUMBERS):
        if num not in string:
            continue
        if min_loc > string.index(num):
            min_loc = string.index(num)
            min_num = str(i + 1)
        if max_loc < string.rindex(num):
            max_loc = string.rindex(num)
            max_num = str(i + 1)
    return min_loc, min_num, max_loc, max_num

def insert_spelled_out(string: str) -> str:
    """Inserts first and last spelled out number of string to string"""
    min_loc, min_num, max_loc, max_num = find_spelled_out(string)
    if max_loc != min_loc:
        string = string[:max_loc] + max_num + string[max_loc:]
    string = string[:min_loc] + min_num + string[min_loc:]
    return string

def part2(data: list[str]) -> int:
    data = [insert_spelled_out(row) for row in data]
    return part1(data)

@stop_watch
def main(data: list[str]) -> None:
    print(f"Part 1 answer: {part1(data)}")
    print(f"Part 2 answer: {part2(data)}")


if __name__ == "__main__":
    data = read_input(1)
    main(data)
