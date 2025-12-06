import functools
import operator
from typing import Callable, Iterable, NamedTuple


class Problem(NamedTuple):
    numbers: Iterable[str]
    operator: str


def parse_input(input: str) -> list[Problem]:
    lines = input.strip().splitlines()

    for j in range(len(lines[0])):
        if all(lines[i][j] == " " for i in range(len(lines))):
            for i in range(len(lines)):
                lines[i] = lines[i][:j] + "," + lines[i][j + 1 :]

    problems = []

    for problem in zip(*[line.split(",") for line in lines]):
        problems.append(Problem(numbers=problem[:-1], operator=problem[-1].strip()))

    return problems


def solution(
    input: str, numbers_transform: Callable[[Iterable[str]], Iterable[int]]
) -> int:
    problems = parse_input(input)

    sum_ = 0

    for problem in problems:
        if problem.operator == "+":
            op, init = operator.add, 0
        elif problem.operator == "*":
            op, init = operator.mul, 1
        else:
            raise ValueError(f"{problem.operator}")

        sum_ += functools.reduce(op, numbers_transform(problem.numbers), init)

    return sum_


def part1(input: str) -> int:
    return solution(input, lambda x: map(int, x))


def part2(input: str) -> int:
    return solution(input, lambda x: (int("".join(i)) for i in zip(*x)))


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
