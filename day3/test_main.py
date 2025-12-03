from .main import part1, part2


INPUT = """\
987654321111111
811111111111119
234234234234278
818181911112111"""


def test_part1():
    assert part1(INPUT) == 357


def test_part2():
    assert part2(INPUT) == 3121910778619


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 17376
    assert part2(input) == 172119830406258
