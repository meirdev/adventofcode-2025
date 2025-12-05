from dataclasses import dataclass

from ranges import Range, RangeSet


@dataclass(frozen=True)
class Database:
    ingredient_id_ranges: list[Range]
    ingredient_ids: list[int]


def parse_input(input: str) -> Database:
    ingredient_id_ranges_input, ingredient_ids_input = input.strip().split("\n\n")

    ingredient_id_ranges = []

    for start, end in map(
        lambda k: k.split("-"), ingredient_id_ranges_input.splitlines()
    ):
        ingredient_id_ranges.append(
            Range(start=int(start), end=int(end), include_end=True)
        )

    ingredient_ids = list(map(int, ingredient_ids_input.splitlines()))

    return Database(
        ingredient_id_ranges=ingredient_id_ranges,
        ingredient_ids=ingredient_ids,
    )


def part1(input: str) -> int:
    db = parse_input(input)

    return sum(
        1 for i in db.ingredient_ids if any(i in r for r in db.ingredient_id_ranges)
    )


def part2(input: str) -> int:
    db = parse_input(input)

    return sum(r.length() + 1 for r in RangeSet(db.ingredient_id_ranges))


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
