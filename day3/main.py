def parse_input(input: str) -> list[list[int]]:
    return [list(map(int, list(line))) for line in input.strip().splitlines()]


def solution(input: str, n: int) -> int:
    banks = parse_input(input)

    joltage = 0

    for batteries in banks:
        to_drop = len(batteries) - n

        stack = []
        for digit in batteries:
            while stack and to_drop > 0 and stack[-1] < digit:
                stack.pop()
                to_drop -= 1
            stack.append(digit)

        stack = stack[:n]

        result = int("".join(map(str, stack)))

        joltage += result

    return joltage


def part1(input: str) -> int:
    return solution(input, 2)


def part2(input: str) -> int:
    return solution(input, 12)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
