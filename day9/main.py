import itertools
import re

from shapely import Point, Polygon


def parse_input(input: str) -> list[tuple[int, int]]:
    return [tuple(map(int, i)) for i in re.findall(r"(\d+),(\d+)", input)]


def area(a, b) -> int:
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)


def part1(input: str) -> int:
    red_tiles = parse_input(input)

    a, b = max(itertools.combinations(red_tiles, 2), key=lambda i: area(i[0], i[1]))

    return area(a, b)


def rect(p1, p2) -> Polygon:
    p1 = Point(*p1)
    p2 = Point(*p2)

    x1, y1 = p1.x, p1.y
    x2, y2 = p2.x, p2.y

    return Polygon([
        Point(x1, y1),
        Point(x1, y2),
        Point(x2, y2),
        Point(x2, y1)
    ])


def part2(input: str) -> int:
    red_tiles = parse_input(input)

    sympy_polygon = Polygon(red_tiles)

    m = 0

    for i in itertools.combinations(red_tiles, 2):
        r = rect(i[0], i[1])
        if sympy_polygon.contains(r):
            m = max(m, area(*i))

    return m


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
