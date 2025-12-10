from .main import part1, part2


INPUT = """\
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""


def test_part1():
    assert part1(INPUT) == 50


def test_part2():
    assert part2(INPUT) == 24


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 4759420470
    assert part2(input) == 1603439684
