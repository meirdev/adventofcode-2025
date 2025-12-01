import re
from collections import deque

START_POINT = 50


def parse_input(input: str) -> list[int]:
    return [
        int(distance) * -1 if rotation == "R" else int(distance)
        for rotation, distance in re.findall(r"(R|L)(\d+)", input)
    ]


def solution(input: str) -> tuple[int, int]:
    rotations = parse_input(input)

    dial = deque([i for i in range(100)])

    dial.rotate(START_POINT)

    zeros_a, zeros_b = 0, 0

    for i in rotations:
        sign = -1 if i < 0 else 1

        i = abs(i)

        for _ in range(i):
            dial.rotate(sign)

            if dial[0] == 0:
                zeros_b += 1

        if dial[0] == 0:
            zeros_a += 1

    return zeros_a, zeros_b


def part1(input: str) -> int:
    zeros_a, _ = solution(input)

    return zeros_a


def part2(input: str) -> int:
    _, zeros_b = solution(input)

    return zeros_b


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
