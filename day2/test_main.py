from .main import part1, part2


INPUT = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""


def test_part1():
    assert part1(INPUT) == 1227775554


def test_part2():
    assert part2(INPUT) == 4174379265


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 38310256125
    assert part2(input) == 58961152806
