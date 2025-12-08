from .main import part1, part2


INPUT = """\
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""


def test_part1():
    assert part1(INPUT, n=10) == 40


def test_part2():
    assert part2(INPUT, n=10) == 25272


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 52668
    assert part2(input) == 1474050600
