from .main import part1, part2


INPUT = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""


def test_part1():
    assert part1(INPUT) == 3


def test_part2():
    assert part2(INPUT) == 6


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 964
    assert part2(input) == 5872
