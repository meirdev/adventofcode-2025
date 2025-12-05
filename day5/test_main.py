from .main import part1, part2


INPUT = """\
3-5
10-14
16-20
12-18

1
5
8
11
17
32"""


def test_part1():
    assert part1(INPUT) == 3


def test_part2():
    assert part2(INPUT) == 14


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 756
    assert part2(input) == 355555479253787
