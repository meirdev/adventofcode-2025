import itertools
import math
from typing import Iterator, NamedTuple, Self

from scipy.cluster.hierarchy import DisjointSet


class Position(NamedTuple):
    x: int
    y: int
    z: int

    def euclidean_distance(self, other: Self) -> float:
        return math.dist(self, other)  # type: ignore


def parse_input(input: str) -> list[Position]:
    return [Position(*map(int, line.split(","))) for line in input.strip().splitlines()]


def solution(
    input: str,
    n: int = 1000,
) -> list[int]:
    positions = parse_input(input)

    disjoint_set = DisjointSet(positions)

    anwser = []

    for i, (a, b) in enumerate(
        sorted(
            itertools.combinations(positions, 2),
            key=lambda i: i[0].euclidean_distance(i[1]),
        )
    ):
        if i == n:
            anwser.append(
                math.prod(sorted(map(len, disjoint_set.subsets()), reverse=True)[:3])
            )

        disjoint_set.merge(a, b)

        if disjoint_set.n_subsets == 1:
            anwser.append(a.x * b.x)
            break

    return anwser


def part1(input: str, n: int = 1000) -> int:
    anwser, _ = solution(input, n)

    return anwser


def part2(input: str, n: int = 1000) -> int:
    _, anwser = solution(input, n)

    return anwser


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
