from .main import part1, part2


INPUT = """\
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""


def test_part1():
    assert part1(INPUT) == 4277556


def test_part2():
    assert part2(INPUT) == 3263827


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 5346286649122
    assert part2(input) == 10389131401929
