from enum import StrEnum
from itertools import product


MOVES = set(product([0, 1, -1], repeat=2)) - {(0, 0)}


class Type(StrEnum):
    EMPTY = "."
    ROLL_OF_PAPER = "@"


def parse_input(input: str) -> dict[tuple[int, int], Type]:
    return {
        (y, x): Type(col)
        for y, row in enumerate(input.strip().splitlines())
        for x, col in enumerate(row)
    }


def solution(input: str, stop_after_one: bool) -> int:
    grid = parse_input(input)

    count = 0

    while True:
        to_remove = set()

        for (y, x), val in grid.items():
            if val == Type.ROLL_OF_PAPER:
                rolls_of_paper = sum(
                    1
                    for (y_, x_) in MOVES
                    if grid.get((y + y_, x + x_)) == Type.ROLL_OF_PAPER
                )

                if rolls_of_paper < 4:
                    to_remove.add((y, x))

        count += len(to_remove)

        for i in to_remove:
            grid.pop(i)

        if len(to_remove) == 0 or stop_after_one:
            break

    return count


def part1(input: str) -> int:
    return solution(input, stop_after_one=True)


def part2(input: str) -> int:
    return solution(input, stop_after_one=False)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
