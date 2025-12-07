from enum import StrEnum


class Type(StrEnum):
    START = "S"
    EMPTY = "."
    SPLITTER = "^"


def parse_input(input: str) -> list[list[Type]]:
    return [list(map(Type, line)) for line in input.strip().splitlines()]


def solution(input: str) -> int:
    grid = parse_input(input)

    split = 0

    beams = [0] * len(grid)

    for row in grid:
        for i, col in enumerate(row):
            if col == Type.START:
                beams[i] = 1

            if col == Type.SPLITTER and beams[i]:
                split += 1

                beams[i - 1] += beams[i]
                beams[i + 1] += beams[i]
                beams[i] = 0

    return split, sum(beams)


def part1(input: str) -> int:
    part1, _ = solution(input)

    return part1


def part2(input: str) -> int:
    _, part2 = solution(input)

    return part2


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
