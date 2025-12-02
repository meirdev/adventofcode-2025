from typing import NamedTuple


class Range(NamedTuple):
    start: int
    end: int


def parse_input(input: str) -> list[Range]:
    return [Range(*map(int, i.split("-"))) for i in input.split(",")]


def part1(input: str) -> int:
    ranges = parse_input(input)

    sum_ = 0

    for start, end in ranges:
        for i in range(start, end + 1):
            num = str(i)

            if len(num) % 2 == 0 and num[: len(num) // 2] == num[len(num) // 2 :]:
                sum_ += i

    return sum_


def part2(input: str) -> int:
    ranges = parse_input(input)

    sum_ = 0

    for start, end in ranges:
        for i in range(start, end + 1):
            num = str(i)

            for k in range(1, len(num) // 2 + 1):
                if len(num) % k == 0 and (num_k := num[:k] * (len(num) // k)) == num:
                    sum_ += int(num_k)
                    break

    return sum_


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
